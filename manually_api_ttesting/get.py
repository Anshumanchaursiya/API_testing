#fetch userdata 1st api from reqres.in website
import requests
import json
import jsonpath

#url
url = "https://reqres.in/api/users/2"

#sending get request
response = requests.get(url)
#print(response)

#parse json
json_response = json.loads(response.text)
#print(json_response)

#fetch value through json path
var1 = jsonpath.jsonpath(json_response,'data')
print(var1[0])
