import MEDIA_EXPERT_parser
import RTV_EURO_AGD_parser
import common_methods

rtv_euro1 = RTV_EURO_AGD_parser.RtvEuroAgdParser('https://www.euro.com.pl/telefony-komorkowe/apple-iphone-13-256gb-red.bhtml')
rtv_euro1.save_details_to_json()
media_expert1 = MEDIA_EXPERT_parser.MediaExpertParser('https://www.mediaexpert.pl/smartfony-i-zegarki/smartfony/smartfon-apple-iphone-13-256gb-5g-6-1-czerwony-mlq93pm-a')

# zgubiłam się już nie wiem, jak włączać funkcje, gdy są we wspólnej klasie