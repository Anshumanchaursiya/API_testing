import xlrd
import json
import requests
import xlwt
import openpyxl

array = ['F1','F2','F3','F4','F5','F6','F7','F8']

########################################
# file location of excell sheet
########################################
file_location = "C:/Users/SONY/Documents/resourse/xl_file/tex2.xlsx"



########################################
#function to update the shheet after testing
########################################
def update(index,output):
    xfile = openpyxl.load_workbook(file_location)
    sheet = xfile["Sheet1"]
    sheet[array[index]] = output
    xfile.save("C:/Users/SONY/Documents/resourse/xl_file/tex2.xlsx")
    xfile.close()


#open the workbook
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)

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

    #writing status code in excel file
    #update(i,status_get)



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

    #writing status code in excel file
    #update(i,status_post)


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

    #writing status code in excel file
    #update(i,status_put)




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

    #writing status code in excel file
    #update(i,status_delete)



#################################################
# extracting the detatils of the api
#################################################

for i in range(sheet.nrows):
    #print(sheet.cell_value(i,0))
    print(i+1,"->")
    url = sheet.cell_value(i,0)
    method = sheet.cell_value(i,1)
    header = sheet.cell_value(i,2)
    body = sheet.cell_value(i,3)
    response = sheet.cell_value(i,4)

    #checking the method
    if(method == "get"):
        get_method(url,header,body,response,i)
    elif(method == "post"):
        post_method(url,header,body,response,i)
    elif(method == "put"):
        put_method(url,header,body,response,i)
    else:
        delete_method(url,header,body,response,i)




