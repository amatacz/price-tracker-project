from datetime import datetime
from pathlib import Path

from bs4 import BeautifulSoup
import requests
import json
import os
import os.path


class Parser():


    def __init__(self, url):
        self.url = url

    def process(self):
        self.response = self.get_response()
        self.soup = self.get_content()
        return self.get_data()


    def get_response(self):
        response = requests.get(self.url, verify=False)
        return response

    def get_content(self):
        html_doc = self.response.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        return soup

    def get_data(self):
        price = self.soup.find("div", {'class': "product-price"}).get('data-price')
        date_and_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

        return {'date': date_and_time, 'price': price}

    # def save_details_to_json(self):
    #     self.ITEM = self.soup.find("div", {'class': 'selenium-product-code'}).contents[0]
    #     date_and_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    #     self.PRICE = float(self.soup.find("div", {'class': "product-price"}).get('data-price'))
    #     self.NAME = self.soup.find("div", {'class': "product-name"}).string.strip()
    #     self.IMG = self.soup.find("a", attrs={"id": "big-photo"}).get('href')

    #     if self.data.get(self.SERVICE):

    #         if not self.data[self.SERVICE].get(self.ITEM):
    #             self.data[self.SERVICE] = {
    #                 self.ITEM: [{"name": self.NAME, "price": self.PRICE, "datetime": date_and_time, "img": self.IMG}]
    #             }
    #         if self.data[self.SERVICE].get(self.ITEM):
    #             self.data[self.SERVICE][self.ITEM].append({"name": self.NAME, "price": self.PRICE, "datetime": date_and_time, "img": self.IMG})

    #     if not self.data.get(self.SERVICE):
    #         self.data[self.SERVICE] = {
    #             self.ITEM: [{"name": self.NAME, "price": self.PRICE, "datetime": date_and_time, "img": self.IMG}]
    #         }

    #     with open(self.json_name, 'w') as file:
    #         json.dump(self.data, file)
