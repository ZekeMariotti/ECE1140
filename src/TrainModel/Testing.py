import csv
import os

print(os.path.abspath(os.curdir))
os.chdir("src/TrainModel")
print(os.path.abspath(os.curdir))

with open("greenLineBlocks.txt", newline = '') as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ',')
    for row in csvReader:
        if (row[0] == "Number"):
            continue
        print("Block Number: ", row[0], " Elevation: ", row[12], " Block Length: ", row[3])