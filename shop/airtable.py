import requests
import json

get_headers = {
    'Authorization': 'Bearer keydq2SURfHCN4Aig'
    }

url = 'https://api.airtable.com/v0/appJeyihmd9jyLKy1/Table?maxRecords=100&view=Orders'
response = requests.get(url, headers=get_headers)
# print(donors_response)
data = response.json()
# print(donors_data)
dumps = json.dumps(data)
# print(dumps)
Orders_list = []

for j in data['records']:
    Orders_list.append(j['fields']['OrderValue'])

print(Orders_list)

sample = f'''{{'order_id': 300}}'''

update_url = 'https://api.airtable.com/v0/appJeyihmd9jyLKy1/TableNew?maxRecords=20&view=Orders'
update_headers = {
    'Authorization': 'Bearer keydq2SURfHCN4Aig',
    'Content-Type': 'application/json'
}
update_data = {
    "fields": {
    # "Name": 33,
    "OrderValue": sample,
    "OrderId": 30,
    },
#   "createdTime": "2021-01-02T20:33:49.000Z"
}

# print(update_data)
update_response = requests.post(update_url, headers=update_headers, json=update_data)



print(Orders_list)

# url= 'http://192.168.43.8/cam-lo.jpg'

# while True:
#     image = urllib.request.urlopen(url)
#     imgnp = np.array(bytearray(image.read()),dtype=np.uint8)
#     img = cv2.imdecode(imgnp, -1)
#     for qrcode in decode(img):
#         myData = qrcode.data.decode('utf-8')
#         print("mydata : ", myData)
#         file1 = open('sample.txt','a')
#         file1.write(myData)         
#         file1.write("\n") 
#         update_url = 'https://api.airtable.com/v0/appJeyihmd9jyLKy1/Table?maxRecords=20&view=Orders'
#         update_headers = {
#             'Authorization': 'Bearer keydq2SURfHCN4Aig',
#             'Content-Type': 'application/json'
#         }
#         update_data = {
#             "fields": {
#             # "Name": 33,
#             "OrderId": myData
#         },
#         #   "createdTime": "2021-01-02T20:33:49.000Z"
#         }
        
#         # print(update_data)
#         update_response = requests.post(update_url, headers=update_headers, json=update_data)
#         pts = np.array([qrcode.polygon],np.int32)
#         pts = pts.reshape((-1,1,2))
#         cv2.polylines(img,[pts],True,(51,255,255),5)
#         pts2 = qrcode.rect
#         cv2.putText(img,myData,(pts2[0],pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,0.9,(51,255,255),2)
#     cv2.imshow('Result : ', img)
#     cv2.waitKey(1)
# cap.release()