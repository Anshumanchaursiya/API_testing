import csv

########################################
# file location of excell sheet
########################################
file_location = "C:/Users/SONY/Documents/automate api testing/cms_api_testing/cms_api_input.csv"

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
out_file = open("C:/Users/SONY/Documents/automate api testing/cms_api_testing/cms_api_output.csv", "w")
in_file = open("C:/Users/SONY/Documents/automate api testing/cms_api_testing/cms_api_input.csv", "rb")
reader = csv.reader(in_file)

#function to update status_method
def update(i,status_method):
    data[i].append(status_method)
    data_str = str(data[i])
    #print(data)
    #writer = csv.writer(sys.stdout)
    #writer.writerow(data_str)
    out_file.write(data_str + "\n")
