#import csv 

#with open ('Dateset.csv','r') as csvToPy: 
 #   csv_reader = csv.reader(csvToPy) 
  #  next(csvToPy)
   # for line in csv_reader:
    #   print(line) 


import pandas as pd 
df = pd.read_csv("Dateset.csv")
#print(df)  

#print(df.head(4)[['Team','Games','Season']])



## Found it guys, use iloc function if you want to modify mutilple rows
print(df.iloc[1])