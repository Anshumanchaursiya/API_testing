import json
import requests
import csv
import sys
import time
import socket
import os
#from resourses.resourse import file_location,reader,row_count,out_file,data,update
import resourses.resourse

input_file_number =0

#first input file
api_name ="input_cms.csv"

#######################################
# GET METHOD
#######################################
def get_method(url,parameter, header, body, response,i):
    print(url)
    print("This is get request")
    if(isinstance(header,str)):
        header = json.loads(header)

    if (isinstance(parameter, str) and parameter != None):
        parameter = json.loads(parameter)

    response_after_get = requests.get(url,params=parameter,headers = header)

    response_list = response_after_get.json()
    print(response_list)
    print(response_after_get.status_code )
    if(response_after_get.status_code == 200):
        status_get = "get response successfully"
    else:
        status_get = "fail to get response"

    #writing status code
    resourses.resourse.update(i,response_after_get.status_code,status_get,response_list)



#######################################
#post method
#######################################
def post_method(url,parameter, header, body, response,i):
    print("this is post method")

    # converting header string to dict formate
    if(isinstance(header,str)):
        header = json.loads(header)

    if (isinstance(parameter, str) and parameter != None):
        parameter = json.loads(parameter)

    response_after_post = requests.post(url,body,params= parameter,headers = header)
    response_list = response_after_post.json()
    print(response_list)
    print(response_after_post.status_code)
    #checking status code
    if(response_after_post.status_code == 201 or response_after_post.status_code == 200):
        status_post = "posted succussfully"
    else:
        status_post = "fail to post"

    #writing status code
    resourses.resourse.update(i,response_after_post.status_code,status_post,response_list)



#######################################
# POST METHOD login
#######################################
def post_method_login(url,parameter, header, body, response,i):

    global api_name
    global input_file_number
    print("this is post method")

    #converting header string to dict format
    if(isinstance(header, str)):
        header = json.loads(header)

    if (isinstance(parameter, str) and parameter != None):
        parameter = json.loads(parameter)

    response_after_post = requests.post(url,body,params = parameter,headers = header)
    response_list = response_after_post.json()
    print(response_list)

    #this token will recieve after login
    #extracting the token from response header
    token_recieve_from_header_response= response_after_post.headers['Authorization']
    body_dict = json.loads(body)
    user_Id = body_dict['emailId']
    header_containing_token = {'token': token_recieve_from_header_response, 'userId': user_Id}

    print(response_after_post.status_code)
    #checking status code
    if(response_after_post.status_code == 201 or response_after_post.status_code == 200):
        status_post = "posted succussfully"
    else:
        status_post = "fail to post"

    resourses.resourse.update(i,response_after_post.status_code,status_post,response_list)

    i=1

    while(i<=resourses.resourse.row_count):
        if(api_name=="input_cms.csv"):
            print(i+1 , "->")
        else:
            print(i,"->")

        url = resourses.resourse.data[i][1]
        method = resourses.resourse.data[i][2]
        parameter = resourses.resourse.data[i][3]
        if(api_name=="input_cms.csv" ):
            header = header_containing_token
        else:
            header = resourses.resourse.data[i][4]
        body = resourses.resourse.data[i][5]
        response = resourses.resourse.data[i][6]

        # checking the method
        if (method == "get"):
            get_method(url,parameter, header, body, response, i)
        elif (method == "post"):
            post_method(url,parameter, header, body, response, i)
        elif (method == "put"):
            put_method(url,parameter, header, body, response, i)
        else:
            delete_method(url,parameter, header, body, response, i)

        input_file_list = os.listdir("C:/Users/SONY/PycharmProjects/framework_api_testing_final/resourses")


        number_of_input_file = len(input_file_list) - 2

        #increasing the value of i to iterate all the rows
        i+=1

        if(i==(resourses.resourse.row_count)):

            i=1;
            input_file_number = input_file_number + 1
            #exit from the loop when all input csv file has been read
            if(input_file_number>=number_of_input_file):
                exit()

            api_name = input_file_list[input_file_number]
            s = api_name
            print("Reading from "+s[6:])
            resourses.resourse.read_write(api_name, "output" +s[5:] )


######################################
# PUT METHOD
######################################
def put_method(url,parameter, header, body, response,i):
    print("this is put method")

    # converting header string to dict formate
    if (isinstance(header, str)):
        header = json.loads(header)

    if (isinstance(parameter, str) and parameter != None):
        parameter = json.loads(parameter)

    response_after_put = requests.put(url, body,params = parameter,headers = header)
    response_list = response_after_put.json()
    print(response_list)
    print(response_after_put.status_code)

    #checking status code
    if(response_after_put.status_code == 200):
        status_put = "modified succfully"
    else:
        status_put = "fail to modify"
    #print(status_put)
    resourses.resourse.update(i,response_after_put.status_code,status_put,response_list)




#############################################
# DELETE METHOD
#############################################
def delete_method(url,parameter, header, body, response,i):

    #converting header string to dict formate
    if (isinstance(header, str)):
        header = json.loads(header)

    if (isinstance(parameter, str) and parameter != None):
        parameter = json.loads(parameter)

    response_after_delete = requests.delete(url,params = parameter,headers = header)
    response_list = response_after_delete.json()
    print(response_list)
    # fetch responce code
    print(response_after_delete.status_code)
    if(response_after_delete.status_code == 204 or response_after_delete.status_code == 200):
        status_delete = "successfully deleted"
    else:
        status_delete = "fail to delete"
    #writing status code
    resourses.resourse.update(i,response_after_delete.status_code,status_delete,response_list)

