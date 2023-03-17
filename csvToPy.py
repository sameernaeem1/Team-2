import pandas as pd 
df = pd.read_csv("Dateset.csv")


df.drop_duplicates()


Teamnum=pd.DataFrame({
'Team':['Chelsea',
'Manchester United','Tottenham'   
 ,'Arsenal'
 ,'Aston Villa'
 ,'Manchester City'
 ,'Liverpool'
 ,'Everton'
,'Birmingham'
,'Sunderland'
,'West Ham'
,'Fulham'
,'Bolton'
,'Stoke'
,'Wigan'
,'Blackburn'
,'Portsmouth'
,'Wolverhampton'
,'Burnley','Hull']
})

## UI 

def Userinterface():
 while True:
    userinput= input("choose the option\nq:Quit\n0:display the whole team in whole season\n1:display the status of each team in whole season\n2:display a team\n3:display team number\n4:compare another team with your choosen team\n5:display the asending order rank of each teams in whole seasons")
    if userinput == '0':
        print(df)

    elif userinput=='q':
       ## quit
       break
    


    elif userinput=='1':
       ##display the status of teams in whole seasons### 
      for index, row in df.iterrows():  
       print(index,row)

    elif userinput=='2':
       ##display the status of that particular team### 

        ui2=input('choose the team:')
        print(df.iloc[int(ui2)])
        chosenteam=df.iloc[int(ui2)]
        ui2_season=input('choose the season')
        print(chosenteam[str(ui2_season)])


    elif userinput=='3':
       ##only shows the unique team##
       for index, row in Teamnum.iterrows():  
        print(index,row ['Team'])

    elif userinput=='4':
  ##Compare 2 different teams, needed to be discussed######
  ##########################################################

      ui4=input('choose the team:')
      print(df.iloc[int(ui4)])

      df1=pd.DataFrame(df.iloc[int(ui4)])

      ui42=input('choose another team to compare with:')
      print(df.iloc[int(ui42)])

      df2=pd.DataFrame(df.iloc[int(ui42)])

      df1.compare(df2)

    elif userinput=='5':
      ## print the whole teams in ascending order of rank.
      print(df.sort_values((['Rank','Points']), ascending=True))


    elif userinput=='6':
       ## print the visualisation
       print () 
    

      



## api workflow
Userinterface()



## components
## sort the list in an specific order 
df.sort_values((['Rank','Points']), ascending=False)
## specify the conditon to find the specific one, rank 1 teams in the past decade
#rank1=df.loc[df['Rank']==1]
#print(rank1)
## iterate through each row
#for index, row in df.iterrows():  ## it list all team at same time, we can use this function to ask which team are they interested in.
# print(index,row ['Team'])

## the rank of arsenal is 3 , which means that permit us to allocate the specific location (R,C)
#print(df.iloc[3,4])

## access unique element
#print(df.head(4)[['Team','Games','Season']])

## use iloc function to modify the associated array
df.iloc[3,1]