import sys
import pprint 

sys.path.append("../")

from ceneo.parser import Parser

p = Parser(url="https://www.ceneo.pl/115151297;0280-0.htm")
pprint.pprint(p.process())