import json
import requests
import csv
import time
import socket
import is_internet_connection
from is_internet_connection import is_connected
from resourses.resourse import file_location,reader,row_count,in_file,out_file,data,update
from api_testing.api_method import post_method_login



#main method
def main():
    print("1->")
    #data is define in the resourse.py file within resourses directory
    #data is the comination of all row of .csv file (from we are reading the api's)
    url = data[0][1]
    method = data[0][2]
    header = data[0][3]

    body = data[0][4]
    response = data[0][5]
    #this method is define in api_method.py file within api_testing folder
    post_method_login(url,header,body,response,0)
    # to close opening file during reading and writing from csv
    #finally close the csv file after reading and writing
    #in_file.close()
    in_file.close()
    #out_file.close()
    out_file.close()


if __name__ == '__main__':
    main()

