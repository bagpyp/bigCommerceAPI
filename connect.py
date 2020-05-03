# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:04:22 2020

@author: web
"""

import requests

url = "https://api.bigcommerce.com/stores/gaywsgumtw/v3/catalog/products?include=variants%2Ccustom_fields"

payload = {}
headers = {
    'x-auth-client': "eptlgcc4vesdj5jp2as53w2gm6iyg7z",
    'x-auth-token': "9ksoui1m1rfkhvdm40zxv4ov605o1cc"
    }

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))














#using github wrapper
"""
import bigcommerce
api = bigcommerce.api.BigcommerceApi\
    (\
        client_id='eptlgcc4vesdj5jp2as53w2gm6iyg7z',\
        store_hash='gaywsgumtw',\
        access_token='9ksoui1m1rfkhvdm40zxv4ov605o1cc'\
    )
        
bigcommerce.bigcommerce
"""