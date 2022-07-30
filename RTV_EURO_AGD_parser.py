from datetime import datetime
import requests
from bs4 import BeautifulSoup

#url = 'https://www.euro.com.pl/telefony-komorkowe/apple-iphone-13-256gb-red.bhtml'
class RTV_EURO_AGD_parser:

    def __init__(self, url):
        self.url = url
        self.request = requests.get(self.url, verify=False)



details = {'RTV EURO AGD': {}}  # {klucz: nazwa sklepu: {klucz - nr.kat : [wartość - słownik ze szczegółami]}


item = soup.find("div", {'class': 'selenium-product-code'}).contents[0]

# datetime.now()
# soup.find("div", {'class': "product-price"}).get('data-price')
# soup.find("div", {'class': "product-name"}).string.strip()



# Nazwa sklepu: sztywno
# Data/godzina: datetime.now()
# Cena:
#         <div class="product-price" data-price="4999.00">
#          <div class="price-normal">
#           4 999 zł
#          </div>
#         </div>
# Nazwa:
#         <div class="product-name">
#          Apple iPhone 13 256GB RED
#         </div>
#
#         nr kat. 1250392


