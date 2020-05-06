# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:04:22 2020

@author: web
"""

import requests
import json


"""GETTING"""

# i = 1 # first page of products
# limit = 250 #upper bound, any reason to decrease?

# url = "https://api.bigcommerce.com/stores/gaywsgumtw/v3/catalog/" \
#     + "products?include=variants%2Ccustom_fields" \
#     + f"&page={i}&limit={limit}" # formatted from i and limit

# headers = {
#     'x-auth-client': "eptlgcc4vesdj5jp2as53w2gm6iyg7z",
#     'x-auth-token': "9ksoui1m1rfkhvdm40zxv4ov605o1cc"
#     } # access tokens

# res = requests.get(url, headers=headers) # actual API call
# data = json.loads(res.content) # rendering json object notation
# products = data['data'] # list of dicts

# n = data['meta']['pagination']['total_pages'] # number of calls for all

# while i < n:
#     i += 1
#     url = "https://api.bigcommerce.com/stores/gaywsgumtw/v3/catalog/" \
#     + "products?include=variants%2Ccustom_fields" \
#     + f"&page={i}&limit={limit}" # formatted from i and limit
#     res = requests.get(url, headers=headers) # actual API call
#     data = json.loads(res.content) # rendering json object notation
#     products.extend(data['data'])

"""PICKLING"""

# with open('products','w') as out:
#     json.dump(products)

"""READING"""

with open('products') as fin:
    products = json.load(fin)













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