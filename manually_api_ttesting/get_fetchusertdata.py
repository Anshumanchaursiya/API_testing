import  requests
import json
import  jsonpath

#API url
url = "https://reqres.in/api/users?page=2"

print(requests.get(url).json())
#send get request
response = requests.get(url).json()
print(response)

'''
#display response contect
#print(response.content)
#print(response.headers)

#parse responce to json format
#json_response = json.loads(response.text)

#print(response)

print(json_response['data'][0])
#to fetch data of a perticular key from json response
print(json_response['total'])


#fetch value using json path (jsonpath is return a list)
data = jsonpath.jsonpath(json_response,'data')
total = jsonpath.jsonpath(json_response,'total')
#print(data[0])
#print(total[1])

#
#print(response.headers.get('Content-Type'))

#assert total[0] == 12

''
