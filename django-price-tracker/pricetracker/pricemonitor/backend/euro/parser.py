from datetime import datetime
from pathlib import Path

from bs4 import BeautifulSoup
import requests
import json
import os
import os.path

from backend.base import BaseParser
from backend.mail_sender import send_email


class Parser(BaseParser):
    SERVICE = "RTV_EURO_AGD"
    ITEM = None
    PRICE = None
    NAME = None
    IMG = None

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
        #self.send_email_with_price_alert()

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
        self.ITEM = self.soup.find("div", {'class': 'selenium-product-code'}).contents[0]
        date_and_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        self.PRICE = float(self.soup.find("div", {'class': "product-price"}).get('data-price'))
        self.NAME = self.soup.find("div", {'class': "product-name"}).string.strip()
        self.IMG = self.soup.find("a", attrs={"id": "big-photo"}).get('href')

        if self.data.get(self.SERVICE):

            if not self.data[self.SERVICE].get(self.ITEM):
                self.data[self.SERVICE] = {
                    self.ITEM: [{"name": self.NAME, "price": self.PRICE, "datetime": date_and_time, "img": self.IMG}]
                }
            if self.data[self.SERVICE].get(self.ITEM):
                self.data[self.SERVICE][self.ITEM].append({"name": self.NAME, "price": self.PRICE, "datetime": date_and_time, "img": self.IMG})

        if not self.data.get(self.SERVICE):
            self.data[self.SERVICE] = {
                self.ITEM: [{"name": self.NAME, "price": self.PRICE, "datetime": date_and_time, "img": self.IMG}]
            }

        with open(self.json_name, 'w') as file:
            json.dump(self.data, file)

    def send_email_with_price_alert(self):
        price_yesterday = self.data[self.SERVICE].get(self.ITEM)[-1].get("price")
        price_today = self.data[self.SERVICE].get(self.ITEM)[-2].get("price")

        if price_yesterday and price_today:
            if price_yesterday >= price_today:
                diff = self.data[self.SERVICE].get(self.ITEM)[-1].get(
                    "price") - self.data[self.SERVICE].get(self.ITEM)[-2].get(
                    "price")

                send_email(self.url, self.SERVICE, diff, self.NAME)
        pass

