import pandas as pd 
df = pd.read_csv("Dateset.csv")

## UI 
def Userinterface():
 while True:
    userinput= input("choose the option\n0:display the whole team in whole season\n1:display the status of each team in whole season\n2:display a team\n3:display team number")
    if userinput == '0':
        print(df)
    elif userinput=='q':
       break
    elif userinput=='1':
      for index, row in df.iterrows():  
       print(index,row)
    elif userinput=='2':
        ui2=input('choose the team:')
        print(df.iloc[int(ui2)])
    elif userinput=='3':
       for index, row in df.iterrows():  
        print(index,row ['Team'])




## workflow
Userinterface()



## components

## sort the list in an specific order 
df.sort_values((['Rank','Points']), ascending=False)
## specify the conditon to find the specific one, rank 1 teams in the past decade
rank1=df.loc[df['Rank']==1]
print(rank1)
## iterate through each row
for index, row in df.iterrows():  ## it list all team at same time, we can use this function to ask which team are they interested in.
 print(index,row ['Team'])

## the rank of arsenal is 3 , which means that permit us to allocate the specific location (R,C)
print(df.iloc[3,4])

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

## access unique element
print(df.head(4)[['Team','Games','Season']])

## use iloc function to modify the associated array
df.iloc[3,1]