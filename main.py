# 'https://www.euro.com.pl/telefony-komorkowe/apple-iphone-13-256gb-red.bhtml'
# 'https://www.mediaexpert.pl/smartfony-i-zegarki/smartfony/smartfon-apple-iphone-13-256gb-5g-6-1-czerwony-mlq93pm-a'
# 'https://mediamarkt.pl/telefony-i-smartfony/smartfon-apple-iphone-13-256gb-product-red-mlq93pm-a'

import importlib

# 'media_markt'
# 'media_markt': [
#     {'product_name': 'Iphone 13 256GB Red',
#      'url': 'https://mediamarkt.pl/telefony-i-smartfony/smartfon-apple-iphone-13-256gb-product-red-mlq93pm-a'}
# ]

# 'media_expert'
# 'media_expert': [
#     {'product_name': 'Iphone 13 256GB Red',
#      'url': 'https://www.mediaexpert.pl/smartfony-i-zegarki/smartfony/smartfon-apple-iphone-13-256gb-5g-6-1'
#             '-czerwony-mlq93pm-a'}
# ]


# 'euro'
# 'euro': [{'product_name': 'Iphone 13 256GB Red',
#           'url': 'https://www.euro.com.pl/telefony-komorkowe/apple-iphone-13-256gb-red.bhtml'}
#          ],

SERVICES = ['euro', 'media_markt', 'media_expert',]

PRODUCTS_MAPPER = {
    'euro': [
        {'product_name': 'Iphone 13 256GB Red', 'url': 'https://www.euro.com.pl/telefony-komorkowe/apple-iphone-13-256gb-red.bhtml'}
    ],
    'media_markt': [
        {'product_name': 'Iphone 13 256GB Red', 'url': 'https://mediamarkt.pl/telefony-i-smartfony/smartfon-apple-iphone-13-256gb-product-red-mlq93pm-a'}
    ],

    'media_expert': [
        {'product_name': 'Iphone 13 256GB Red', 'url': 'https://www.mediaexpert.pl/smartfony-i-zegarki/smartfony/smartfon-apple-iphone-13-256gb-5g-6-1-czerwony-mlq93pm-a'}
    ],
}


def main():
    for service in SERVICES:
        for product_info in PRODUCTS_MAPPER[service]:
            parser = importlib.import_module(f"backend.{service}.parser")
            obj = parser.Parser(
                url=product_info['url'],
                product_name=product_info['product_name']
            )
            obj.process()


if __name__ == "__main__":
    main()
