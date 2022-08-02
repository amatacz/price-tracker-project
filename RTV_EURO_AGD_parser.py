from datetime import datetime, date
from pathlib import Path

from bs4 import BeautifulSoup
import requests
import json
import os
import os.path


class RtvEuroAgdParser:
    SHOP_NAME = 'RTV_EURO_AGD'
    DETAILS_DICTS = []

    def get_response(self):
        response = requests.get(self.url, verify=False)  # wywołuję 2 razy url - gdzie on w sumie powinien siedzieć??
        return response

    def get_content(self):
        html_doc = self.get_response().text
        soup = BeautifulSoup(html_doc, 'html.parser')
        return soup

    def __init__(self, url):
        self.status_code = None
        self.url = url
        self.status_code = RtvEuroAgdParser.get_response(self).status_code
        self.soup = RtvEuroAgdParser.get_content(self)
        self.html_name = os.getcwd() + '/' + RtvEuroAgdParser.SHOP_NAME + '/html_' + date.today().strftime('%d-%m-%Y') + '.txt'

        with open(self.html_name, 'w', encoding='utf-8') as output:
            output.write(self.soup.prettify())

    def save_details_to_json(self):

        item = self.soup.find("div", {'class': 'selenium-product-code'}).contents[0]
        date_and_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        price = self.soup.find("div", {'class': "product-price"}).get('data-price')
        name = self.soup.find("div", {'class': "product-name"}).string.strip()
        details = {'RTV_EURO_AGD': {item: [name, price, date_and_time]}}
        json_name = os.getcwd() + '/' + RtvEuroAgdParser.SHOP_NAME + '/json_' + date.today().strftime('%d-%m-%Y') + '.json'

        with open(json_name, 'w') as json_file:
            json.dump(details, json_file)

        return json_file

    @staticmethod
    def append_new_data_to_json():

        path = str(os.getcwd() + '\\' + RtvEuroAgdParser.SHOP_NAME + '\\')
        os.chdir(path)
        files = Path(os.getcwd()).glob('*.json')
        for file in files:
            with open(str(file), 'r') as fp:
                data = json.load(fp)

            RtvEuroAgdParser.DETAILS_DICTS.append(data)
        return RtvEuroAgdParser.DETAILS_DICTS


