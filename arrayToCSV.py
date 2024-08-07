import csv
from pathlib import Path

def write2DArrToCSV(startArr: list, name: str, path: str = "") -> str:
    name = "{0}.csv".format(name)
    if path != "":
        name = path + "/" + name
        directory = Path(name)
        directory.parent.mkdir(parents=True, exist_ok=True)
    with open((name),  "w+", newline='') as my_csv:
        writer = csv.writer(my_csv, delimiter=',')
        for row in startArr:
            writer.writerow(row)
    return name


a = [[1, 2, 3, 4], [5, 666, 7, 8]]
filename = "Heck"
mypath = "jjj/sd"
write2DArrToCSV(a, filename, mypath)
