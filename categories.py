# -*- coding: utf-8 -*-
"""
Created on Sun May  3 18:15:28 2020
@author: Robert Cunningham
"""

import requests
import json

"""GETTING"""

# url = "https://api.bigcommerce.com/stores/gaywsgumtw/v3/catalog/" \
#     + "categories?is_visible=true&limit=250" \


# headers = {
#     'x-auth-client': "eptlgcc4vesdj5jp2as53w2gm6iyg7z",
#     'x-auth-token': "9ksoui1m1rfkhvdm40zxv4ov605o1cc"
#     } # access tokens

# res = requests.get(url, headers=headers) # actual API call
# data = json.loads(res.content) # rendering json object notation

"""PICKLING"""

# with open('categories','w') as out:
#     json.dumps(data['data'])

"""READING"""
with open('categories') as fin:
   categories = json.load(fin)