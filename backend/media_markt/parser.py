from datetime import datetime
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import json
import os

from backend.base import BaseParser
from backend.mail_sender import send_email


class Parser(BaseParser):
    SERVICE = 'MEDIA_MARKT'
    ITEM = None
    PRICE = None
    NAME = None

    def __init__(self, url, product_name):
        self.url = url
        self.product_name = product_name
        self.json_name = Path(os.getcwd() + '/data/' + self.SERVICE + '.json')
        self.process()

    def process(self):
        self.response = self.get_response()
        self.data = self.get_data()
        self.save_details_to_json()
        #self.send_email_with_price_alert()

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
        date_and_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        try:
            self.ITEM = self.response.find_element(By.XPATH, '//*[@id=\"21607324\"]/div[1]/div[1]/div[1]/div[1]/div/span').text
        except NoSuchElementException:
            pass

        try:
            self.PRICE = float(self.response.find_element(By.CLASS_NAME, "whole").text)
        except NoSuchElementException:
            pass

        try:
            self.NAME = self.response.find_element(By.XPATH, '//*[@id=\"21607324\"]/div[1]/div[1]/div[1]/div[1]/h1').text
        except NoSuchElementException:
            pass

        if self.data.get(self.SERVICE):
            if not self.data[self.SERVICE].get(self.ITEM):
                self.data[self.SERVICE] = {
                    self.ITEM: [{'name': self.NAME, 'price': self.PRICE, 'datetime': date_and_time}]
                }
            if self.data[self.SERVICE].get(self.ITEM):
                self.data[self.SERVICE][self.ITEM].append({'name': self.NAME, 'price': self.PRICE, 'datetime': date_and_time})

        if not self.data.get(self.SERVICE):
            self.data[self.SERVICE] = {
                self.ITEM: [{'name': self.NAME, 'price': self.PRICE, 'datetime': date_and_time}]
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





