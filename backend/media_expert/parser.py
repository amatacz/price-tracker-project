from datetime import datetime
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import os

from backend.base import BaseParser


class Parser(BaseParser):
    SERVICE = 'MEDIA_EXPERT'

    def __init__(self, url, product_name):
        self.url = url
        self.product_name = product_name
        self.json_name = Path(os.getcwd() + '/data/' + self.SERVICE + '.json')
        self.process()

    def process(self):
        self.response = self.get_response()
        self.data = self.get_data()
        self.save_details_to_json()

    def get_response(self):
        response = webdriver.Chrome('C:/Users/matacza/Downloads/chromedriver')
        response.get(self.url)

        return response

    def get_data(self):
        self.json_name.touch(exist_ok=True)
        with open(self.json_name, 'r') as file:
            content = file.read()
            if content:
                return json.loads(content)
        return {}

    def save_details_to_json(self):
        item = self.response.find_element(By.XPATH, "//*[@id=\"section_title\"]/span").text
        date_and_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        price = self.response.find_element(By.XPATH, "//*[@id=\"section_offer-available\"]/div[1]/div[1]/div/div/span[1]").text
        name = self.response.find_element(By.XPATH, "//*[@id=\"section_title\"]/div[1]/h1").text

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


