import pandas as pd 
df = pd.read_csv("Dateset.csv")
print(df)  

#print(df.head(4)[['Team','Games','Season']])

## top 10 team
Chelsea=df.iloc[0]
Manchester_united=df.iloc[1]
Tottenham=df.iloc[2]
Arsenal=df.iloc[3]
AstonVilla=df.iloc[4]
Manchester_city=df.iloc[5]
Liverpool=df.iloc[6]
Everton=df.iloc[7]
Birmingham=df.iloc[8]
sunderland=df.iloc[9]
westHam=df.iloc[10]

## Found it guys, use iloc function if you want to modify mutilple rows

df.iloc[3,1]

## this means that the rank of arsenal is 3 , which means that permit us to allocate the specific location (R,C)
print(df.iloc[3,4])
## iterate through each row
for index, row in df.iterrows():  ## it list all team at same time, we can use this function to ask which team are they interested in.
 print(index,row ['Team'])

## specify the conditon to find the specific one, rank 1 teams in the past decade
rank1=df.loc[df['Rank']==1]
print(rank1)

## sort the list in an specific order 
df.sort_values((['Rank','Points']), ascending=False)

## details of each team
for index, row in df.iterrows():  
 print(index,row)