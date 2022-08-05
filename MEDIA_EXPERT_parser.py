from datetime import datetime, date
from pathlib import Path

from bs4 import BeautifulSoup
import requests
import json
import os
import os.path
import common_methods





class MediaExpertParser():
    SHOP_NAME = 'MEDIA_EXPERT'
    DETAILS_DICTS = []

    def get_response(self):
        response = requests.get(self.url, verify=False)
        return response

    def get_content(self):
        html_doc = self.get_response().text
        soup = BeautifulSoup(html_doc, 'html.parser')
        return soup

    def __init__(self, url):
        self.status_code = None
        self.url = url
        self.status_code = MediaExpertParser.get_response(self).status_code
        self.soup = MediaExpertParser.get_content(self)
        self.html_name = os.getcwd() + '\\' + MediaExpertParser.SHOP_NAME + '\html_' + date.today().strftime('%d-%m-%Y') + '.txt'

        try:
            with open(self.html_name, 'w', encoding='utf-8') as output:
                output.write(self.soup.prettify())
        except FileNotFoundError:
            os.mkdir(os.getcwd() +'\\' + MediaExpertParser.SHOP_NAME)
            with open(self.html_name, 'w', encoding='utf-8') as output:
                output.write(self.soup.prettify())

    def save_data_to_json(self):
        item = self.soup.find("div", attrs={'span class': "id is-regular"})
        date_and_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        price = self.soup.find("div", {'class_': "prices"})
        name = self.soup.find("div", {'h1 class': "name is-title"})
        details = {'MEDIA_EXPERT': {item: [name, price, date_and_time]}}
        json_name = os.getcwd() + '/' + MediaExpertParser.SHOP_NAME + '/json_' + date.today().strftime('%d-%m-%Y') + '.json'

        with open(json_name, 'w') as json_file:
            json.dump(details, json_file)

        return json_file
