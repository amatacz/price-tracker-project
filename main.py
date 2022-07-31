import RTV_EURO_AGD_parser


rtv_euro1 = RTV_EURO_AGD_parser.RtvEuroAgdParser('https://www.euro.com.pl/telefony-komorkowe/apple-iphone-13-256gb-red.bhtml')

print(rtv_euro1.append_new_data_to_json())

