from datetime import datetime, date
from bs4 import BeautifulSoup
import requests
import json

# czy nie narobiłam za dużo tych zmiennych w konstruktorze?


class RtvEuroAgdParser:

    def __init__(self, url):
        self.url = url
        self.request = requests.get(self.url, verify=False)
        self.details = {'RTV_EURO_AGD': {}} # to w konstruktorze czy powyżej?

        self.html_doc = self.request.text
        self.soup = BeautifulSoup(self.html_doc, 'html.parser')

        self.item = self.soup.find("div", {'class': 'selenium-product-code'}).contents[0]
        self.datetime = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        self.price = self.soup.find("div", {'class': "product-price"}).get('data-price')
        self.name = self.soup.find("div", {'class': "product-name"}).string.strip()
        self.txt_name = r'C:/Users/matacza/Desktop/Projekt1/RTV_EURO_AGD/html_' + date.today().strftime('%d-%m-%Y') + '.txt'
        self.json_name = r'C:/Users/matacza/Desktop/Projekt1/RTV_EURO_AGD/json_' + date.today().strftime('%d-%m-%Y') + '.json'

        with open(self.txt_name, 'w', encoding='utf-8') as output:
            output.write(self.soup.prettify())

    def update_and_save_to_json(self):
        updated = self.details['RTV_EURO_AGD'].update({self.item: [self.name, self.price, self.datetime]})
        with open(self.json_name, 'w') as jd:
            json.dump(updated, jd)

        return jd # gdy go otwiram jest nullem - WHY?;<