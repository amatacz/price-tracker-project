from datetime import datetime, date
from pathlib import Path

from bs4 import BeautifulSoup
import requests
import json
import os
import os.path

# tu Selenium? wylapuje mnie jako bota - jak żyć?
# https://mediamarkt.pl/telefony-i-smartfony/smartfon-apple-iphone-13-256gb-product-red-mlq93pm-a
class MediaMarktParser:
    SHOP_NAME = 'MEDIA_MARKT'
    DETAILS_DICTS = []

    def get_response(self):
        response = requests.get(self.url, verify=False)  # wywołuję 2 razy url - gdzie on w sumie powinien siedzieć??
        return response

    def get_content(self):
        html_doc = self.get_response().text
        soup = BeautifulSoup(html_doc, 'html.parser')
        return soup

    def __init__(self, url):
        self.status_code = None
        self.url = url
        self.status_code = MediaMarktParser.get_response(self).status_code
        self.soup = MediaMarktParser.get_content(self)
        self.html_name = os.getcwd() + '\\' + MediaMarktParser.SHOP_NAME + '\html_' + date.today().strftime('%d-%m-%Y') + '.txt'

        try:
            with open(self.html_name, 'w', encoding='utf-8') as output:
                output.write(self.soup.prettify())
        except FileNotFoundError:
            os.mkdir(os.getcwd() +'\\' + MediaMarktParser.SHOP_NAME)
            with open(self.html_name, 'w', encoding='utf-8') as output:
                output.write(self.soup.prettify())


