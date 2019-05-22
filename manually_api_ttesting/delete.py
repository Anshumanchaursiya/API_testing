import requests
import json
import jsonpath

url = "https://reqres.in/api/users/2"

response = requests.delete(url)

#fetch responce code
print(response.status_code)

#validating the response code
asser
