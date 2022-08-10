import requests
from getpass import getpass
from django.contrib.auth import logout
from django.http import HttpRequest
from requests import request
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

auth_endpoint = "http://127.0.0.1:8000/api/auth/"
username = input("What is your username?\n")
password = getpass()
auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Bearer {token}"
    }
    endpoint = "http://127.0.0.1:8000/api/products/"

    get_request = requests.get(endpoint, headers=headers)  # HTTP request

       # get_request = requests.get(endpoint)  # HTTP request
        # print(get_request.text)  # print raw text response
        # print(get_request.status_code)

    print(get_request.json())