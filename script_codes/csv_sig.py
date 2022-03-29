import os
import csv

basePath = './data/csv/csv'
sigPath = './data/csv/csv_sig'

fileList = os.listdir(basePath)

for file in fileList:
    with open(os.path.join(basePath,file),'r',encoding='utf-8') as csvFile:
        csvReader = csv.reader(csvFile)
        with open(os.path.join(sigPath,file),'w',encoding='utf_8_sig') as csvFile:
            csvWriter = csv.writer(csvFile)
            for row in csvReader:
                csvWriter.writerow(row)
        



