import json
import requests
import csv
import sys

########################################
# file location of excell sheet
########################################
file_location = "C:/Users/SONY/Documents/resourse/cms_api_csv/cms_api.csv"

#################################################
# extracting the detatils of the api
#################################################
data = []
with open(file_location,"r") as f:

    reader = csv.reader(f,delimiter = ',')
    data = list(reader)
    row_count = len(data)
    #for val in data:
     #    print (val[0])
    #print(data,"################################")

##########################################
#function to update the sheet after testing
##########################################
out_file = open("C:/Users/SONY/Documents/resourse/cms_api_csv/validated.csv", "w")
in_file = open("C:/Users/SONY/Documents/resourse/cms_api_csv/cms_api.csv", "rb")
reader = csv.reader(in_file)


#function to update status_method
def update(i,status_method):
    data[i].append(status_method)
    data_str = str(data[i])
    #print(data)
    #writer = csv.writer(sys.stdout)
    #writer.writerow(data_str)
    out_file.write(data_str + "\n")

#######################################
# GET METHOD
######################################

def get_method(url, header, body, response,i):
    #print(type(header))
    print("This is get request")
    #print(header,"**************************")
    response_after_get = requests.get(url,headers = header)
    print(response_after_get.json())
    #json.dumps(header)
    #print(type(header))

    print(response_after_get.status_code ," ok")
    if(requests.get(url,header).status_code == 200):
        status_get = "get response successfully"
    else:
        status_get = "fail to get response"
    print(status_get)

    #writing status code
    update(i,status_get)

#######################################
# POST METHOD
#######################################

def post_method(url, header, body, response,i):
    print(type(header))
    print("this is post method")
    #print(header,"**********************")
    request_json = json.loads(body)
    ######told by mam
    #data = {'emailId': 'priyanka.pitla@datami.com', 'password': 'wynk123'}
    #y = json.dumps(data, sort_keys=True, indent=4)
    ######
    header_json = header

    if(isinstance(header_json, str)):
        header_json = json.loads(header)

    header_string = json.dumps(header)
    print(type(header_string))
    json_header = json.dumps(header_string)
    #print(header_string,'**')
    #response_after_post = requests.post(url, request_json, headers=header_json)
    #print(type(header_json))
    print(type(header))
    response_after_post = requests.post(url,body,headers = header_json)
    print(response_after_post.json())
    if('Authorization' in response_after_post.headers):
        token_recieve_from_header_response= response_after_post.headers['Authorization']
        user_Id = request_json['emailId']
        local_data = {'token': token_recieve_from_header_response, 'userId': user_Id}
    #else:
     #   print("hii")
      #  local_data = header
       # print(i)

    #user_Id = request_json['emailId']


    #making json string of header to send the requests for other apis key will be token and user_id
    #first creating empty list
    #local_data = {}
    #local_data['token'] = token_recieve_from_header_response
    #local_data['userId'] = user_Id

    #local_data = {'token': header[0], 'userId': user_Id}

    #header_json_data = json.dumps(local_data)

    #print(token_recieve_from_header_response)
    #print(response_after_post.json())
    print(response_after_post.status_code)
    #checking status code
    if(response_after_post.status_code == 201 or response_after_post.status_code == 200):
        status_post = "posted succussfully"
    else:
        status_post = "fail to post"
    print(status_post)

    #writing status code
    update(i,status_post)

    ####################################################
    #after this post(login) every api get call
    ####################################################
    #print(data,"********************")
    local_data =
    for i in range(1,row_count):
        print(i + 1, "->")
        url = data[i][0]
        method = data[i][1]
        header = local_data
        body = data[i][3]
        response = data[i][4]

        # checking the method
        if (method == "get"):
            get_method(url, header, body, response, i)
        elif (method == "post"):
            post_method(url, header, body, response, i)
        elif (method == "put"):
            put_method(url, header, body, response, i)
        else:
            delete_method(url, header, body, response, i)


######################################
# PUT METHOD
######################################

def put_method(url, header, body, response,i):
    print("this is put method")
    requests_json_put = json.loads(body)
    response_after_put = requests.put(url, requests_json_put)
    print(response_after_put.json())
    print(response_after_put.status_code)

    #checking status code
    if(response_after_put.status_code == 200):
        status_put = "modified succfully"
    else:
        status_put = "fail to modify"
    print(status_put)

    #writing status code
    update(i,status_put)




#############################################
# DELETE METHOD
#############################################

def delete_method(url, header, body, response,i):
    response_after_delete = requests.delete(url,headers = header)
    # fetch responce code
    print(response_after_delete.status_code)
    if(response_after_delete.status_code == 204 or response_after_delete.status_code == 200):
        status_delete = "successfully deleted"
    else:
        status_delete = "fail to delete"
    print(status_delete)

    #writing status code
    update(i,status_delete)


###################################
#post 1st method post(login) AND
##################################
#main method
##################################
def main():
    print("1->")
    url = data[0][0]
    method = data[0][1]
    header = data[0][2]
    body = data[0][3]
    response = data[0][4]
    post_method(url,header,body,response,0)
    # to close opening file during reading and writing from csv
    in_file.close()
    out_file.close()

if __name__ == '__main__':
    main()
















'''

for i in range(row_count):
    print(i+1,"->")
    url = data[i][0]
    method = data[i][1]
    header = data[i][2]
    body = data[i][3]
    response = data[i][4]

    #checking the method
    if(method == "get"):
        get_method(url,header,body,response,i)
    elif(method == "post"):
        post_method(url,header,body,response,i)
    elif(method == "put"):
        put_method(url,header,body,response,i)
    else:
        delete_method(url,header,body,response,i)

'''















