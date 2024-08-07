import csv
from pathlib import Path

def write2DArrToCSV(startArr: list, name: str, path: str = "") -> str:
    name = "{0}.csv".format(name)
    if path != "" :
        name = path + "/" + name
        directory = Path(name)
        directory.parent.mkdir(parents=True, exist_ok=True)
    with open((name), "w+") as my_csv:
        writer = csv.writer(my_csv, delimiter=',')
        writer.writerows(startArr)
    return name


# a = [[1, 2, 3, 4], [5, 6, 7, 8]]
# filename = "Heck"
# mypath = "jjj/sd/"
# write2DArrToCSV(a, filename, mypath)
