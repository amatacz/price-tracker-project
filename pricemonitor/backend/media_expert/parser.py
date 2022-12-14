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
        chrome_options.add_argument("start-maximized")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        response = uc.Chrome('./backend/chromedriver.exe', chrome_options=chrome_options)
        response.get(self.url)

        return response

    def get_data(self):
        price = None
        try:
            confirmation_click = WebDriverWait(self.response, 10).until(exp.element_to_be_clickable((By.XPATH, "//*[@id='cf-stage']/div[6]/label/span")))
            confirmation_click.click()
        except TimeoutException:
            try:
                human_click = WebDriverWait(self.response, 10).until(exp.element_to_be_clickable((By.XPATH, "//*[@id='challenge-stage']/div/input")))
                human_click.click()
            except:
                pass
            # confirmation_click = WebDriverWait(self.response, 10).until(exp.element_to_be_clickable((By.XPATH, "//*[@id='cf-stage']/div[6]/label/span")))
            # confirmation_click.click()
        
        #cookies_close = WebDriverWait(self.response, 10).until(exp.element_to_be_clickable((By.XPATH, "//*[@id='fastcookie']/div[1]/div/button/span"))).click()
        
        try:
            price = WebDriverWait(self.response, 10).until(exp.presence_of_element_located((By.XPATH, "//*[@id='section_offer-available']/div[2]/div[1]/div/div/span[1]"))).text
        except TimeoutException:
            pass

        date_and_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

        return {'date': date_and_time, 'price': price}





# class Parser(BaseParser):
#     SERVICE = 'MEDIA_EXPERT'
#     ITEM = None
#     PRICE = None
#     NAME = None
#     IMG = None

#     def __init__(self, url, product_name):
#         self.url = url
#         self.product_name = product_name
#         self.json_name = Path(os.getcwd() + '/data/' + self.SERVICE + '.json')
#         self.process()

#     def process(self):
#         self.response = self.get_response()
#         self.data = self.get_data()
#         self.save_details_to_json()
#         #self.send_email_with_price_alert()

#     def get_response(self):
#         response = webdriver.Chrome('C:/Users/matacza/Downloads/chromedriver')
#         response.get(self.url)

#         return response

#     def get_data(self):
#         self.json_name.touch(exist_ok=True)
#         with open(self.json_name, 'r') as file:
#             content = file.read()
#             if content:
#                 return json.loads(content)
#         return {}

#     def save_details_to_json(self):
#         try:
#             self.ITEM = self.response.find_element(By.XPATH, "//*[@id=\"section_title\"]/span").text
#         except NoSuchElementException:
#             pass

#         date_and_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
#         try:
#             self.PRICE = float((self.response.find_element(By.XPATH, "//*[@id=\"section_offer-available\"]/div[1]/div[1]/div/div/span[1]").text).replace("\u202f", ""))
#             # self.PRICE = self.response.find_element(By.XPATH, "//*[@id=\"section_page-summary-box\"]/div/div[2]/div/div[2]/div[1]/div/div/span[1]").text
#         except NoSuchElementException:
#             pass

#         try:
#             self.NAME = self.response.find_element(By.XPATH, "//*[@id=\"section_title\"]/div[1]/h1").text
#         except NoSuchElementException:
#             pass

#         try:
#             self.IMG = self.response.find_element(By.XPATH, "//*[@id=\"section_product-gallery\"]/div[1]/div[2]/div[1]/div/div/div[1]/div/div/div[1]").get_attribute('src')
#         except NoSuchElementException:
#             pass

#         if self.data.get(self.SERVICE):
#             if not self.data[self.SERVICE].get(self.ITEM):
#                 self.data[self.SERVICE] = {
#                     self.ITEM: [{'name': self.NAME, 'price': self.PRICE, 'datetime': date_and_time, "img": self.IMG}]
#                 }
#             if self.data[self.SERVICE].get(self.ITEM):
#                 self.data[self.SERVICE][self.ITEM].append({'name': self.NAME, 'price': self.PRICE, 'datetime': date_and_time, "img": self.IMG})

#         if not self.data.get(self.SERVICE):
#             self.data[self.SERVICE] = {
#                 self.ITEM: [{'name': self.NAME, 'price': self.PRICE, 'datetime': date_and_time, "img": self.IMG}]
#             }

#         with open(self.json_name, 'w') as file:
#             json.dump(self.data, file)

#     def send_email_with_price_alert(self):
#         price_yesterday = self.data[self.SERVICE].get(self.ITEM)[-1].get("price")
#         price_today = self.data[self.SERVICE].get(self.ITEM)[-2].get("price")

#         if price_yesterday and price_today:
#             if price_yesterday >= price_today:
#                 diff = self.data[self.SERVICE].get(self.ITEM)[-1].get(
#                     "price") - self.data[self.SERVICE].get(self.ITEM)[-2].get(
#                     "price")

#                 send_email(self.url, self.SERVICE, diff, self.NAME)
#         pass





