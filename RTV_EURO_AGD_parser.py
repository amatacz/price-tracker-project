from datetime import datetime, date
from pathlib import Path

from bs4 import BeautifulSoup
import requests
import json
import os
import os.path


class RtvEuroAgdParser:

    def __init__(self, url):
        self.url = url
        self.request = requests.get(self.url, verify=False)

        self.html_doc = self.request.text
        self.soup = BeautifulSoup(self.html_doc, 'html.parser')

        self.item = self.soup.find("div", {'class': 'selenium-product-code'}).contents[0]
        self.datetime = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        self.price = self.soup.find("div", {'class': "product-price"}).get('data-price')
        self.name = self.soup.find("div", {'class': "product-name"}).string.strip()
        self.details = {'RTV_EURO_AGD': {self.item: [self.name, self.price, self.datetime]}}
        self.html_name = os.getcwd() + '/RTV_EURO_AGD/html_' + date.today().strftime('%d-%m-%Y') + '.txt'
        self.txt_name = os.getcwd() + '/RTV_EURO_AGD/txt_' + date.today().strftime('%d-%m-%Y') + '.txt'
        self.json_name = os.getcwd() + '/RTV_EURO_AGD/json_' + date.today().strftime('%d-%m-%Y') + '.json'

        with open(self.html_name, 'w', encoding='utf-8') as output:
            output.write(self.soup.prettify())

    def save_details_to_json_and_txt(self):
        with open(self.txt_name, 'w') as txf:
            txf.write(json.dumps(self.details))

        with open(self.json_name, 'w') as jf:
            json.dump(self.details, jf)

    @staticmethod
    def append_new_data_to_json():
        path = str(os.getcwd() + '\\RTV_EURO_AGD\\')
        os.chdir(path)
        files = Path(os.getcwd()).glob('*.json')

        details_dicts = []
        for file in files:
            with open(str(file), 'r') as fp:
                data = json.load(fp)

            details_dicts.append(data)
        return details_dicts
