from datetime import datetime
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
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
        response = webdriver.Chrome('./backend/chromedriver.exe', chrome_options=chrome_options)
        response.get(self.url)

        return response

    def get_data(self):
        try:
            price = WebDriverWait(self.response, 10).until(exp.visibility_of_element_located((By.XPATH, "//*[@id='21607324']/div[2]/button/span/div/span"))).text
        except NoSuchElementException:
            pass
        date_and_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

        return {'date': date_and_time, 'price': price}
