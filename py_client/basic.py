import requests
from pprint import pprint

# endpoint = 'https://httpbin.org/status/200/'
# endpoint = 'https://httpbin.org/anything'
endpoint = "http://localhost:8000/api/v1/"

get_response = requests.get(endpoint, params={"product_id": 123})
# print(get_response.text)
pprint(get_response.json())
# pprint(get_response.status_code)
