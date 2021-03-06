import csv
import api_testing.api_method
########################################
# file location
########################################
data = []
CSVWriter = ''
row_count = 0
in_file = ''
out_file = ''
import codecs
def read_write(input_file, output_file):
    global in_file
    in_file = "C:/Users/SONY/PycharmProjects/framework_api_testing_final/resourses/" + input_file

    with open(in_file, "r",encoding='utf-8') as f:
        #reader = csv.reader(codecs.open(f, 'rU', 'utf-16'))
        reader = csv.reader(f, delimiter=',')
        global data
        data = list(reader)
        global row_count
        row_count = len(data)
        global out_file

    out_file = "C:/Users/SONY/PycharmProjects/framework_api_testing_final/out/" + output_file
    out_file = open(out_file, "w",encoding="utf-8", newline='')
    in_file = open(in_file, "rb")
    reader = csv.reader(in_file)
    global CSVWriter
    CSVWriter = csv.writer(out_file)

    CSVWriter.writerow(["*SERIAL NO.*", "***URL***", "***REQUEST TYPE***","***QUERY PARAMETER***","***HEADER***", "*** REQUEST BODY***","***EXPECTED STATUS CODE***", "***ACTUAL STATUS CODE***", "***VALIDATION***", "***RESPONSE***"])



##########################################
#function to update the sheet after testing
##########################################
def update(i,status_code,status_method,response):
    data[i].append(status_code)
    data[i].append(status_method)
    data[i].append(response)
    CSVWriter.writerow(data[i])
