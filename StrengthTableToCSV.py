import WebScraper, arrayToCSV

const_website = "https://strengthlevel.com/strength-standards/"

def scrapeToCSV(exerciseType: str, name: str):
    resultTable = WebScraper.getStrengthTable(const_website+name)
    arrayToCSV.write2DArrToCSV(resultTable, name, exerciseType)


#scrapeToCSV("Barbell", "barbell-curl")
file = open("BarbellExercises.txt", "r")
for line in file:
    #print(line.replace("\n", ""))
    scrapeToCSV(exerciseType="Barbell", name=line.replace("\n", ""))

