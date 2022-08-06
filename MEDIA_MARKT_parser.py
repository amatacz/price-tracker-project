from datetime import datetime, date
import json
import os
import os.path

from selenium import webdriver
from selenium.webdriver.common.by import By


class MediaMarktParser:
    driver = webdriver.Chrome('C:/Users/matacza/Downloads/chromedriver')
    driver.get('https://mediamarkt.pl/telefony-i-smartfony/smartfon-apple-iphone-13-256gb-product-red-mlq93pm-a')

    SHOP_NAME = 'MEDIA_MARKT'
    DETAILS_DICTS = []
    #
    # def get_response(self):
    #     response = requests.get(self.url, verify=False)  # wywołuję 2 razy url - gdzie on w sumie powinien siedzieć??
    #     return response
    #
    # def get_content(self):
    #     html_doc = self.get_response().text
    #     soup = BeautifulSoup(html_doc, 'html.parser')
    #     return soup
    #
    # def __init__(self, url):
    #     self.status_code = None
    #     self.url = url
    #     self.status_code = MediaMarktParser.get_response(self).status_code
    #     self.soup = MediaMarktParser.get_content(self)
    #     self.html_name = os.getcwd() + '\\' + MediaMarktParser.SHOP_NAME + '\html_' + date.today().strftime(
    #         '%d-%m-%Y') + '.txt'
    #
    #     try:
    #         with open(self.html_name, 'w', encoding='utf-8') as output:
    #             output.write(self.soup.prettify())
    #     except FileNotFoundError:
    #         os.mkdir(os.getcwd() + '\\' + MediaMarktParser.SHOP_NAME)
    #         with open(self.html_name, 'w', encoding='utf-8') as output:
    #             output.write(self.soup.prettify())



    def save_data_to_json(self):
        item = self.driver.find_element(By.CLASS_NAME, 'catalog').text[-7:-1] # na to na pewno jest ładniejszy sposób, niż cyferka po cyferce?
        date_and_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        price = self.driver.find_element(By.CLASS_NAME, 'whole').text
        name = self.driver.find_element(By.TAG_NAME, "h1").text

        details = {MediaMarktParser.SHOP_NAME: {item: [name, price, date_and_time]}}
        json_name = os.getcwd() + '/' + MediaMarktParser.SHOP_NAME + '/json_' + date.today().strftime('%d-%m-%Y') + '.json'

        try:
            with open(json_name, 'w') as json_file:
                json.dump(details, json_file)
        except FileNotFoundError:
            os.mkdir(os.getcwd() + '\\' + MediaMarktParser.SHOP_NAME)
            with open(json_name, 'w') as json_file:
                json.dump(details, json_file)

        return json_file




