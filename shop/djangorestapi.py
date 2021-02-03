import urllib.request

import requests
import json

# get_headers = {
#     'Authorization': 'Bearer keydq2SURfHCN4Aig'
#     }

# url = 'http://127.0.0.1:8000/shop/all_products/'
# response = requests.get(url)
# # print("response",response)
# data = response.json()
# # print(data)
# dumps = json.dumps(data)
# # # print(dumps)



# products_list = []

# for j in data['records']:
#     products_list.append(j['fields']['OrderId'])

# print("products_list",products_list)

update_url = 'http://127.0.0.1:8000/shop/all_orders_create/'
update_headers = {
'Allow': 'PUT', 'OPTIONS'
'Content-Type': 'application/json'
}
update_data = {
        "seller": 6,
        "status": "Delivered"
    }

# [

    
    # ]
        

# print(update_data)
update_response = requests.post(update_url, headers=update_headers, json=update_data)

# AIRTABLE-PYTHON INTEGRATION ENDS