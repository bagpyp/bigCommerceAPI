# -*- coding: utf-8 -*-
"""
Created on Sun May  3 18:26:41 2020
@author: Robert Cunningham
"""

import requests
import json
import pandas as pd

"""GETTING"""

# url = "https://api.bigcommerce.com/stores/gaywsgumtw/v3/catalog/" \
#     + "categories/tree" 
    
# headers = {
#     'x-auth-client': "eptlgcc4vesdj5jp2as53w2gm6iyg7z",
#     'x-auth-token': "9ksoui1m1rfkhvdm40zxv4ov605o1cc"
#     } # access tokens

# res = requests.get(url, headers=headers) # actual API call
# data = json.loads(res.content) # rendering json object notation
# tree = data['data'] # list of dicts


# df = pd.DataFrame(tree)
# df.to_pickle('tree')

"""READING"""

df = pd.read_pickle('tree')