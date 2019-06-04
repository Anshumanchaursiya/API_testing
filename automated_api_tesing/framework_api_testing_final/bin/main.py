import json
import requests
import csv
import socket
import is_internet_connection
from is_internet_connection import is_connected

#from resourses.resourse import file_location,reader,row_count,in_file,out_file,data,update
import resourses.resourse
#from api_testing.test import post_method_login
import api_testing.api_method
from api_testing.api_method import api_name



#main method
def main():
    print("1->")
    resourses.resourse.read_write("input_cms.csv", "output_cms.csv")
    #data is define in the resourse.py file within resourses directory
    #data is the comination of all row of .csv file (from we are reading the api's)
    url = resourses.resourse.data[0][1]
    method = resourses.resourse.data[0][2]
    parameter = resourses.resourse.data[0][3]
    header = resourses.resourse.data[0][4]
    body = resourses.resourse.data[0][5]
    response = resourses.resourse.data[0][6]
    #this method is define in api_method.py file within api_testing folder
    api_testing.api_method.post_method_login(url, parameter, header, body, response, 0)


    #finally close the csv file after reading and writing
    resourses.resourse.in_file.close()
    resourses.resourse.out_file.close()


if __name__ == '__main__':
    main()

