import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as exp
from selenium.webdriver.support.ui import WebDriverWait

# chrome_options = Options()
# chrome_options.headless = True
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--window-size=1920x1080")
response = webdriver.Chrome('./backend/chromedriver.exe')
response.get("https://www.ceneo.pl/115151297;0280-0.htm")

services = ['mediamarkt.pl', 'mediaexpert.pl', 'euro.com.pl']
d ={}
offers = response.find_elements(By.CSS_SELECTOR, ".product-offer__container.clickable-offer.js_offer-container-click.js_product-offer")
for offer in offers:
    for service in services:
        if offer.get_attribute('data-shopurl') == service:
            d[service] = {'price': offer.get_attribute('data-price')}
print(d)


