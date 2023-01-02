# URL https://www.ceneo.pl/115151297;0280-0.htm

from datetime import datetime
from pathlib import Path

import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as exp
from selenium.webdriver.support.ui import WebDriverWait

import json
import os


class Parser():
    def __init__(self, url):
        self.url = url
        self.process()

    def process(self):
        self.response = self.get_response()
        return self.get_data()

    def get_response(self):
        chrome_options = Options()
        chrome_options.headless = True
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920x1080")
        response = webdriver.Chrome('./backend/chromedriver.exe')
        response.get(self.url)

        return response

    def get_data(self):
        services = ['mediamarkt.pl', 'mediaexpert.pl', 'euro.com.pl']
        date_and_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        d ={}
        offers = self.response.find_elements(By.CSS_SELECTOR, ".product-offer__container.clickable-offer.js_offer-container-click.js_product-offer")
        for offer in offers:
            for service in services:
                if offer.get_attribute('data-shopurl') == service:
                    d[service] = {'price': offer.get_attribute('data-price'), 'date': date_and_time}

        return d