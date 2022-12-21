import sys
import pprint 

sys.path.append("../")

from media_expert.parser import Parser

p = Parser(url="https://www.mediaexpert.pl/smartfony-i-zegarki/smartfony/smartfon-apple-iphone-13-256gb-5g-6-1-czerwony-mlq93pm-a")
pprint.pprint(p.process())