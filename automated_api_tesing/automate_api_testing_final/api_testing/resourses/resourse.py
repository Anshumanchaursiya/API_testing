import csv

########################################
# file location of excell sheet
########################################
#file_location = "C:/Users/SONY/Documents/automate api testing/cms_api_testing/cms_api_input.csv"
file_location = "C:/Users/SONY/PycharmProjects/automate_api_testing_final/resourses/input_cms.csv"
#################################################
# extracting the detatils of the api
#################################################
data = []
with open(file_location,"r") as f:

    reader = csv.reader(f,delimiter = ',')
    data = list(reader)
    row_count = len(data)


##########################################
#function to update the sheet after testing
##########################################

out_file = open("C:/Users/SONY/PycharmProjects/automate_api_testing_final/out/output_cms.csv","w",newline='')

in_file = open("C:/Users/SONY/PycharmProjects/automate_api_testing_final/resourses/input_cms.csv","rb")
reader = csv.reader(in_file)

CSVWriter = csv.writer(out_file)
CSVWriter.writerow(["*SERIAL NO.*","***URL***", "***REQUEST TYPE***", "***HEADER***","*** REQUEST BODY***","***EXPECTED STATUS CODE***","***ACTUAL STATUS CODE***","***VALIDATION***","***RESPONSE***"])
#function to update status_method
def update(i,status_code,status_method,response):
    data[i].append(status_code)
    data[i].append(status_method)
    if(isinstance(response,dict)):
        list(response)
    #print(type(response))

    data[i].append(response)

    #with open("C:/Users/SONY/PycharmProjects/automate_api_testing_final/out/output_cms.csv", "w") as Output_csv:
    #CSVWriter = csv.writer(out_file)
    CSVWriter.writerow(data[i])
    #print(data[i])


    #data_str = ",".join(data[i])
    #print(type(data_list))
    #print(data)


    #out_file.write(data_str + "\n")
    #out_file.write(','.join(data_str))
    #writer = csv.writer(out_file)


