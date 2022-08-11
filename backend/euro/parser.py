from datetime import datetime, date
from pathlib import Path

from bs4 import BeautifulSoup
import requests
import json
import os
import os.path

from backend.base import BaseParser


class Parser(BaseParser):
    SERVICE = 'RTV_EURO_AGD'

    def __init__(self, url, product_name):
        self.url = url
        self.product_name = product_name
        self.json_name = Path(os.getcwd() + '/data/' + self.SERVICE + '.json')
        self.process()

    def process(self):
        self.response = self.get_response()
        self.status_code = self.response.status_code
        self.soup = self.get_content()
        self.data = self.get_data()
        self.save_details_to_json()


    def get_response(self):
        response = requests.get(self.url, verify=False)
        return response

    def get_content(self):
        html_doc = self.response.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        return soup

    def get_data(self):
        self.json_name.touch(exist_ok=True)
        with open(self.json_name, 'r') as file:
            content = file.read()
            if content:
                return json.loads(content)
        return {}

    def save_details_to_json(self):
        item = self.soup.find("div", {'class': 'selenium-product-code'}).contents[0]
        date_and_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        price = self.soup.find("div", {'class': "product-price"}).get('data-price')
        name = self.soup.find("div", {'class': "product-name"}).string.strip()

        if self.data.get(self.SERVICE):

            if not self.data[self.SERVICE].get(item):
                self.data[self.SERVICE] = {
                    item: [{'name': name, 'price': price, 'datetime': date_and_time}]
                }
            if self.data[self.SERVICE].get(item):
                self.data[self.SERVICE][item].append({'name': name, 'price': price, 'datetime': date_and_time})

        if not self.data.get(self.SERVICE):
            self.data[self.SERVICE] = {
                item: [{'name': name, 'price': price, 'datetime': date_and_time}]
            }

        with open(self.json_name, 'w') as file:
            json.dump(self.data, file)

