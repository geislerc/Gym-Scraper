import WebScraper
from Library import arrayToCSV

const_website = "https://strengthlevel.com/strength-standards/"

def scrapeToCSV(exerciseType: str, name: str):
    resultTable = WebScraper.getStrengthTable(const_website + name)
    arrayToCSV.write2DArrToCSV(resultTable, name, exerciseType)


#scrapeToCSV("Barbell", "barbell-curl")
file = open("../ExerciseLists/CableExercises.txt", "r")
for line in file:
    #print(line.replace("\n", ""))
    scrapeToCSV(exerciseType="Cable", name=line.replace("\n", ""))

