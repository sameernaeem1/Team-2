import csv 

with open ('movies.csv','r') as csv_file: 
    csv_reader = csv.reader(csv_file) 
    next(csv_file)
    for line in csv_reader:
       print(line) 


print("Top Movies of the Decade")