import csv


# a = [[1,2,3,4],[5,6,7,8]]
#
# with open("new_file.csv","w+") as my_csv:
#     csvWriter = csv.writer(my_csv,delimiter=',')
#     csvWriter.writerows(a)

def write2DArrToCSV(startArray, name):
    name = name + ".csv"
    with open((name), "w+") as my_csv:
        writer = csv.writer(my_csv, delimiter=',')
        writer.writerows(startArray)
    return name


# a = [[1,2,3,4],[5,6,7,8]]
# filename = "Heck"
# write2DArrToCSV(a, filename)