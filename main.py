from datetime import datetime
import requests
from bs4 import BeautifulSoup


url = 'https://www.euro.com.pl/telefony-komorkowe/apple-iphone-13-256gb-red.bhtml'
request = requests.get(url, verify=False)

html_doc = request.text
soup = BeautifulSoup(html_doc, 'html.parser')

with open('html.txt', 'w', encoding='utf-8') as output:
    output.write(soup.prettify())

details = {} # {klucz: nazwa sklepu: {klucz - nr.kat : [wartość - słownik ze szczegółami]}


# datetime.now()
# soup.find("div", {'class': "product-price"}).get('data-price')
# soup.find("div", {'class': "product-name"}).string.strip()


'''
Nazwa sklepu: sztywno
Data/godzina: datetime.now()
Cena:
        <div class="product-price" data-price="4999.00">
         <div class="price-normal">
          4 999 zł
         </div>
        </div>
Nazwa: 
        <div class="product-name">
         Apple iPhone 13 256GB RED
        </div>
        
        nr kat. 1250392
'''

