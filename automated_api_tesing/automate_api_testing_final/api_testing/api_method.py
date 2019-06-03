import json
import requests
import csv
import sys
import time
import socket

from resourses.resourse import file_location,reader,row_count,out_file,data,update



#######################################
# GET METHOD
######################################

def get_method(url, header, body, response,i):


    #print(type(header))
    print("This is get request")
    #print(header,"**************************")

    response_after_get = requests.get(url,headers = header)

    response_list = response_after_get.json()
    print(response_list)
    #json.dumps(header)
    #print(type(header))

    print(response_after_get.status_code )
    if(response_after_get.status_code == 200):
        status_get = "get response successfully"
    else:
        status_get = "fail to get response"
    #print(status_get)

    #writing status code
    update(i,response_after_get.status_code,status_get,response_list)



#######################################
#post method
#######################################
def post_method(url, header, body, response,i):
    print("this is post method")
    #print(header,"**********************")
    #request_json = json.loads(body)
    header_json = header

    if(isinstance(header_json, str)):
        header_json = json.loads(header)

    #header_string = json.dumps(header)
    #print(type(header_string))
    #json_header = json.dumps(header_string)
    #print(type(header))
    #print(header)
    response_after_post = requests.post(url,body,headers = header)
    response_list = response_after_post.json()
    print(response_list)
    print(response_after_post.status_code)
    #checking status code
    if(response_after_post.status_code == 201 or response_after_post.status_code == 200):
        status_post = "posted succussfully"
    else:
        status_post = "fail to post"
    #print(status_post)

    #writing status code
    update(i,response_after_post.status_code,status_post,response_list)



#######################################
# POST METHOD login
#######################################

def post_method_login(url, header, body, response,i):
    #print(type(header))
    print("this is post method")
    #print(header,"**********************")
    request_json = json.loads(body)
    header_json = header

    if(isinstance(header_json, str)):
        header_json = json.loads(header)

    header_string = json.dumps(header)
    #print(type(header_string))
    json_header = json.dumps(header_string)
    #print(header_string,'**')
    #response_after_post = requests.post(url, request_json, headers=header_json)
    #print(type(header_json))
    #print(type(header))
    response_after_post = requests.post(url,body,headers = header_json)
    response_list = response_after_post.json()
    print(response_list)
    #if('Authorization' in response_after_post.headers):
    token_recieve_from_header_response= response_after_post.headers['Authorization']
    user_Id = request_json['emailId']
    local_data = {'token': token_recieve_from_header_response, 'userId': user_Id}

    print(response_after_post.status_code)
    #checking status code
    if(response_after_post.status_code == 201 or response_after_post.status_code == 200):
        status_post = "posted succussfully"
    else:
        status_post = "fail to post"

    update(i,response_after_post.status_code,status_post,response_list)

    ####################################################
    #after this post(login) every api get call
    ####################################################
    #print(data,"********************")
    #print(row_count)
    for i in range(1,row_count):
        print(i+1 , "->")
        url = data[i][1]
        method = data[i][2]
        header = local_data
        body = data[i][4]
        response = data[i][5]

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
    #print(type(header))
    #time.sleep(5)
    response_after_put = requests.put(url, body,headers = header)
    response_list = response_after_put.json()
    print(response_list)
    print(response_after_put.status_code)

    #checking status code
    if(response_after_put.status_code == 200):
        status_put = "modified succfully"
    else:
        status_put = "fail to modify"
    #print(status_put)

    #writing status code
    update(i,response_after_put.status_code,status_put,response_list)




#############################################
# DELETE METHOD
#############################################

def delete_method(url, header, body, response,i):
    response_after_delete = requests.delete(url,headers = header)
    response_list = response_after_delete.json()
    print(response_list)
    # fetch responce code
    print(response_after_delete.status_code)
    if(response_after_delete.status_code == 204 or response_after_delete.status_code == 200):
        status_delete = "successfully deleted"
    else:
        status_delete = "fail to delete"
    #print(status_delete)

    #writing status code
    update(i,response_after_delete.status_code,status_delete,response_list)

'''
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
    post_method_login(url,header,body,response,0)
    # to close opening file during reading and writing from csv
    in_file.close()
    out_file.close()

if __name__ == '__main__':
    main()

'''