from datetime import datetime, date
from pathlib import Path

import json
import os
import os.path
import RTV_EURO_AGD_parser
import MEDIA_EXPERT_parser


class CommonMethods:

    def append_new_data_to_json(self):
        path = str(os.getcwd() + '\\' + self.SHOP_NAME + '\\')
        os.chdir(path)
        files = Path(os.getcwd()).glob('*.json')
        for file in files:
            with open(str(file), 'r') as fp:
                data = json.load(fp)

            self.DETAILS_DICTS.append(data)
        return self.DETAILS_DICTS
