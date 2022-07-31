import RTV_EURO_AGD_parser


rtv_euro1 = RTV_EURO_AGD_parser.RtvEuroAgdParser('https://www.euro.com.pl/telefony-komorkowe/apple-iphone-13-256gb-red.bhtml')

rtv_euro1.update_and_save_to_json_and_txt()
print(rtv_euro1.details)
