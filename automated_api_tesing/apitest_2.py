import json
import requests
import csv
import sys

########################################
# file location of excell sheet
########################################
file_location = "C:/Users/SONY/Documents/resourse/csv_file/tex2.csv"


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



##########################################
#function to update the sheet after testing
##########################################
out_file = open("C:/Users/SONY/Documents/resourse/csv_file/updated.csv", "w")
in_file = open("C:/Users/SONY/Documents/resourse/csv_file/tex2.csv", "rb")
reader = csv.reader(in_file)
#function to update status_method
def update(i,status_method):
    data[i].append(status_method)
    data_str = str(data[i])

    #writer = csv.writer(sys.stdout)
    #writer.writerow(data_str)
    out_file.write(data_str + "\n")

    #print(type(lst_to_string),"**********",type(data_str))
#######################################
# GET METHOD
######################################

def get_method(url, header, body, response,i):
    print("This is get request")
    print(requests.get(url).json())
    if(requests.get(url).status_code == 200):
        status_get = "pass"
    else:
        status_get = "fail"
    print(status_get)

    #writing status code
    update(i,status_get)

#######################################
# POST METHOD
#######################################

def post_method(url, header, body, response,i):
    print("this is post method")
    request_json = json.loads(body)
    response_after_post = requests.post(url, request_json)
    print(response_after_post.json())
    print(response_after_post.status_code)
    #checking status code
    if(response_after_post.status_code == 201):
        status_post = "posted succussfully"
    else:
        status_post = "fail"
    print(status_post)

    #writing status code
    update(i,status_post)


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
        status_put = "done"
    else:
        status_put = "fail"
    print(status_put)

    #writing status code
    update(i,status_put)




#############################################
# DELETE METHOD
#############################################

def delete_method(url, header, body, response,i):
    response_after_delete = requests.delete(url)
    # fetch responce code
    print(response_after_delete.status_code)
    if(response_after_delete.status_code == 204):
        status_delete = "successfully deleted"
    else:
        status_delete = "fail"
    print(status_delete)

    #writing status code
    update(i,status_delete)



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

#to close opening file during reading and writing from csv
in_file.close()
out_file.close()



