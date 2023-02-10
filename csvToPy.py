import csv 

with open ('footballDataset.csv','r') as csvToPy: 
    csv_reader = csv.reader(csvToPy) 
    next(csvToPy)
    for line in csv_reader:
       print(line) 