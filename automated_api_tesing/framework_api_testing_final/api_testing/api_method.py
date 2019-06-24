import json
import requests
import csv
import sys
import time
import socket
import os
#from resourses.resourse import file_location,reader,row_count,out_file,data,update
import resourses.resourse
import Config.Api_Conf
import glob

input_file_number = 0
response_list =[]
response_after_get = ""
response_after_post = ""
response_after_put = ""
response_after_delete = ""

#first input file
api_name ="input_cms.csv"

#######################################
# GET METHOD
#######################################
def get_method(url,parameter, header, body, response,i):
    print("GET", end =" ")
    if(isinstance(header,str) and header!=None):
        header = json.loads(header)

    if (isinstance(parameter, str)):
        parameter = json.loads(parameter)

    try:
        global response_after_get
        response_after_get = requests.get(url,params=parameter,headers = header,timeout = Config.Api_Conf.SETTIME)

        if (response_after_get.headers['content-type'] == 'text/html; charset=utf-8'):
            print(response_after_get)
        else:
            global response_list
            response_list = response_after_get.json()
            print(response_after_get)
            # print(response_list)

        # print(response_after_get.status_code )
        if (response_after_get.status_code == 200):
            status_get = "PASS"
        else:
            status_get = "FAIL"

        # writing status code
        resourses.resourse.update(i, response_after_get.status_code, status_get, response_list)
    except requests.Timeout as err:
        print("Timeout")
        resourses.resourse.update(i, "Timeout", "Timeout", "Timeout")







#######################################
#POST METHOD
#######################################
def post_method(url,parameter, header, body, response,i):
    print("POST", end =" ")

    # converting header string to dict formate
    if(isinstance(header,str)):
        header = json.loads(header)

    if (isinstance(parameter, str) and parameter != None):
        parameter = json.loads(parameter)

    try:
        global response_after_post
        response_after_post = requests.post(url,body,params= parameter,headers = header,timeout = Config.Api_Conf.SETTIME)


        response_list = response_after_post.json()
        #print(response_list)
        print(response_after_post)
        #checking status code
        if(response_after_post.status_code == 201 or response_after_post.status_code == 200):
            status_post = "PASS"
        else:
            status_post = "FAIL"

        #writing status code
        resourses.resourse.update(i,response_after_post.status_code,status_post,response_list)
    except requests.Timeout as err:
        print("Timeout")
        resourses.resourse.update(i, "Timeout", "Timeout", "Timeout")



#######################################
# POST METHOD login
#######################################
def post_method_login(url,parameter, header, body, response,i):

    global api_name
    global input_file_number
    print("POST", end =" ")

    #converting header string to dict format
    if(isinstance(header, str)):
        header = json.loads(header)

    if (parameter != None and isinstance(parameter, str) ):
        parameter = json.loads(parameter)

    response_after_post = requests.post(url,body,params = parameter,headers = header)
    response_list = response_after_post.json()
    #print(response_list)

    #this token will recieve after login
    #extracting the token from response header
    token_recieve_from_header_response= response_after_post.headers['Authorization']


    print(response_after_post)
    #checking status code
    if(response_after_post.status_code == 201 or response_after_post.status_code == 200):
        status_post = "PASS"
    else:
        status_post = "FAIL"

    resourses.resourse.update(i,response_after_post.status_code,status_post,response_list)

    i=1

    while(i<=resourses.resourse.row_count):
        if(api_name=="input_cms.csv"):
            print(i+1 , "->", end = " ")
        else:
            print(i,"->", end= " ")

        url = resourses.resourse.data[i][1]
        method = resourses.resourse.data[i][2]
        parameter = resourses.resourse.data[i][3]
        if(api_name=="input_cms.csv" or api_name=="input_negative_cms.csv" ):
            # converting header string to dict format
            if (isinstance(resourses.resourse.data[i][4], str)):
                resourses.resourse.data[i][4] = json.loads(resourses.resourse.data[i][4])

            user_Id = resourses.resourse.data[i][4]["userId"]

            header_containing_token = {'token': token_recieve_from_header_response, 'userId': user_Id}
            header = header_containing_token
        else:
            header = resourses.resourse.data[i][4]
        body = resourses.resourse.data[i][5]
        response = resourses.resourse.data[i][6]

        # checking the method
        try:

            if (method == "get"):
                get_method(url,parameter, header, body, response, i)
            elif (method == "post"):
                post_method(url,parameter, header, body, response, i)
            elif (method == "put"):
                put_method(url,parameter, header, body, response, i)
            else:
                delete_method(url,parameter, header, body, response, i)
        except:
            print("something error found")


        #list of all csv file inside resourses folder
        extension = 'csv'
        os.chdir(Config.Api_Conf.INPUT_FILE_PATH)
        input_file_list = glob.glob(('*.{}'.format(extension)))

        #sort all the file
        input_file_list.sort()

        #removing the pycache file that is not necessary
        if "__pycache__" in input_file_list:
            input_file_list.remove('__pycache__')

        #total number of file in resourse folder
        number_of_input_file = len(input_file_list)

        #print(number_of_input_file,"######")

        #increasing the value of i to iterate all the rows
        i+=1

        if(i==(resourses.resourse.row_count)):
            i=1



            #exit from the loop when all input csv file has been read
            if(input_file_number==number_of_input_file):
                exit()

            if (input_file_list[input_file_number] == 'input_cms.csv'):
                input_file_number = input_file_number + 1

            api_name = input_file_list[input_file_number]
            input_file_number += 1
            s = api_name
            print("\nReading from "+s[6:])

            #read_write function is in resourse.py file inside resourse folder
            resourses.resourse.read_write(api_name, "output" +s[5:] )



######################################
# PUT METHOD
######################################
def put_method(url,parameter, header, body, response,i):
    print("PUT", end =" ")

    # converting header string to dict formate
    if (isinstance(header, str)):
        header = json.loads(header)

    if (isinstance(parameter, str) and parameter != None):
        parameter = json.loads(parameter)

    try:
        global response_after_put
        response_after_put = requests.put(url, body,params = parameter,headers = header,timeout = Config.Api_Conf.SETTIME)
        response_list = response_after_put.json()
        #print(response_list)
        print(response_after_put)

        #checking status code
        if(response_after_put.status_code == 200):
            status_put = "PASS"
        else:
            status_put = "FAIL"
        #print(status_put)
        resourses.resourse.update(i,response_after_put.status_code,status_put,response_list)
    except requests.Timeout as err:
        print("Timeout")
        resourses.resourse.update(i, "Timeout", "Timeout", "Timeout")




#############################################
# DELETE METHOD
#############################################
def delete_method(url,parameter, header, body, response,i):
    print("DELETE", end = " ")
    #converting header string to dict formate
    if (isinstance(header, str)):
        header = json.loads(header)

    if (isinstance(parameter, str) and parameter != None):
        parameter = json.loads(parameter)

    try:
        global response_after_delete
        response_after_delete = requests.delete(url,params = parameter,headers = header,timeout = Config.Api_Conf.SETTIME)
        response_list = response_after_delete.json()
        #print(response_list)
        # fetch responce code
        print(response_after_delete)
        if(response_after_delete.status_code == 204 or response_after_delete.status_code == 200):
            status_delete = "PASS"
        else:
            status_delete = "FAIL"
        #writing status code
        resourses.resourse.update(i,response_after_delete.status_code,status_delete,response_list)
    except requests.Timeout as err:
        print("Timeout")
        resourses.resourse.update(i, "Timeout", "Timeout", "Timeout")
