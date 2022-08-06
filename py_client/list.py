import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

endpoint = "http://127.0.0.1:8000/api/products/"

# get_request = requests.get(endpoint, json={"product_id": 123})  # HTTP request

get_request = requests.get(endpoint)  # HTTP request
# print(get_request.text)  # print raw text response
# print(get_request.status_code)

print(get_request.json())