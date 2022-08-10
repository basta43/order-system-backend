import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
headers = {'Authorization': 'Bearer d68ba509fa40e4c33c6f9658f471979099b727d9'}
endpoint = "http://127.0.0.1:8000/api/products/"

# get_request = requests.get(endpoint, json={"product_id": 123})  # HTTP request
data = {"title": "basta43", "price": 100.99}
get_request = requests.post(endpoint, json=data, headers=headers)  # HTTP request
# print(get_request.text)  # print raw text response
# print(get_request.status_code)

print(get_request.json())