# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:08:50 2020
@author: Robert Cunningham
"""

import bigcommerce
api = bigcommerce.api.BigcommerceApi\
    (\
        client_id='eptlgcc4vesdj5jp2as53w2gm6iyg7z',\
        store_hash='gaywsgumtw',\
        access_token='9ksoui1m1rfkhvdm40zxv4ov605o1cc'\
    )
        
api.Products.iterall().next()
