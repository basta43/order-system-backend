import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
product_id = input("What is the product id you want to delete? ")
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} is not a valid id')

if(product_id):
    endpoint = f"http://127.0.0.1:8000/api/products/{product_id}/delete/"

# get_request = requests.get(endpoint, json={"product_id": 123})  # HTTP request
get_response = requests.delete(endpoint)  # HTTP request
# print(get_request.text)  # print raw text response
# print(get_request.status_code)

print(get_response.status_code, get_response.status_code == 204)

