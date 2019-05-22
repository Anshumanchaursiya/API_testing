#this is for post method
import requests
import json
import jsonpath

url = "https://reqres.in/api/users"

#Read input json file
file = open('post.json')

json_input = file.read()

#json.loads = type cast
request_json = json.loads(json_input)
response = requests.post(url,request_json)

#validating Responce
assert response.status_code == 201

#fetch header from the responce
#print(response.headers)
print(response.headers.get('Content-Type'))

#parse response into the json format
response_json = json.loads(response.text)
