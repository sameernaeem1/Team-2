import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("Dataset.csv")


# get a list of all team names
team_names = df['Team'].unique().tolist()


## UI 
1
def Userinterface():
 while True:
    print("-----Premier League Season's 2009 to 2022-----")
    print()
    userinput= input("1:Display Teams\n2:Compare Teams\n3:Choose Team\nQ:Quit\nChoose an Option:")
    if userinput == '1':
        for i, team in enumerate(team_names):
         print(f"{i+1}. {team}")



    #VISUALISATION
    elif userinput=='2':
      for i, team in enumerate(team_names):
        print(f"{i+1}. {team}")
      chosen_team_index1 = int(input("Enter the  number of the team you want to select")) - 1
      chosen_team1 = team_names[chosen_team_index1]
      print(f"First Team Picked:{chosen_team1}")
      chosen_team_df1=df[df['Team'] == chosen_team1]
      chosen_team_index2 = int(input("Enter the number of the team you want to compare it with")) - 1
      chosen_team2 = team_names[chosen_team_index2]
      print(f"Second Team Picked:{chosen_team2}")
      chosen_team_df2=df[df['Team'] == chosen_team2]
      user_keyword=input("Which keyword would you like to compare between the teams:(eg Points, rank or wins)\n")
      chosen_columns1=[col for col in chosen_team_df1.columns if user_keyword.lower() in col.lower()]
      chosen_columns2=[col for col in chosen_team_df2.columns if user_keyword.lower() in col.lower()]
      a=chosen_team_df1[chosen_columns1].values.tolist()
      b=chosen_team_df2[chosen_columns2].values.tolist()
      c=chosen_team_df1['Season'].values.tolist()
      print(a)
      print(b)
      print(c)

      fig, ax = plt.subplots()
      fig.suptitle("Comparing", fontsize=22)
      ax.set_title(chosen_team1 + " vs " + chosen_team2,fontsize=18)
      ax.set_xlabel("Year",fontsize=16)
      ax.set_ylabel(user_keyword, fontsize=16)
      ax.plot(c,a,'ro--',label=chosen_team1)
      ax.plot(c,b,'go--',label=chosen_team2)
      ax.grid(True)
      ax.legend()
      ax.set_xlim(-0.05, 12.05)
      plt.show()



    elif userinput=='3':
       for i, team in enumerate(team_names):
         print(f"{i+1}. {team}")
       chosen_team_index = int(input("Enter the number of the team you want to select: ")) - 1
       chosen_team = team_names[chosen_team_index]
       print(f"Team Picked:{chosen_team}")
       chosen_team_df=df[df['Team'] == chosen_team]
       user_keyword=input("Enter a keyword to search for the component of the team:(eg Points, rank or wins)\n")
       chosen_columns=[col for col in chosen_team_df.columns if user_keyword.lower() in col.lower()]
       a=chosen_team_df[chosen_columns].values.tolist()
       c=chosen_team_df['Season'].values.tolist()
        
       print(a)
       print(c)
       

       fig, ax = plt.subplots()
       ax.set_title(chosen_team,fontsize=14)
       ax.set_xlabel("Year",fontsize=12)
       ax.set_ylabel(user_keyword, fontsize=10)
       ax.plot(c,a,'mD:',label=chosen_team)
       ax.grid(True)

       ax.legend()
       plt.show()

    elif userinput=='4':
       for i, team in enumerate(team_names):
         print(f"{i+1}. {team}")
       chosen_team_index = int(input("Enter the number of the team you want to select: ")) - 1
       chosen_team = team_names[chosen_team_index]
       print(f"Team Picked:{chosen_team}")
       chosen_team_df=df[df['Team'] == chosen_team]
       user_keyword=input("Enter a keyword to search for the component of the team:(eg Points, rank or wins)\n")
       chosen_columns=[col for col in chosen_team_df.columns if user_keyword.lower() in col.lower()]
       items_count=chosen_team_df[chosen_columns].values.tolist()
       rangeOf_item=chosen_team_df['Season'].values.tolist()
        
      


       fig, ax = plt.subplots()
       ax.set_title(chosen_team,fontsize=14)
       ax.set_xlabel("Year",fontsize=12)
       ax.set_ylabel(user_keyword, fontsize=10)
       ax.bar(items_count,rangeOf_item, width=1)
       ax.grid(True)
       
       ax.legend()
       plt.show()
        
       
       



       if  user_keyword =='wins':
        totalnum=chosen_team_df[chosen_columns].sum()
        print(f"{chosen_team}  get {totalnum} ")
       elif user_keyword=='rank':
        print(f"{chosen_team} got different {user_keyword} in different season for {len(chosen_team_df) } times")
       elif user_keyword=='points':
        totalpoints=chosen_team_df[chosen_columns].sum()
        print(f"{chosen_team} got total {totalpoints} points")

   
    elif userinput=='q' or userinput=='Q':
       ## quit
       break
    
   # elif userinput=='00':
       ##display the status of teams in whole seasons### 
   #  for index, row in df.iterrows():  
    #   print(index,row)

    elif userinput=='20':
##display the status of that particular team### 
      print("Select a team:")
      for i, team in enumerate(team_names):
         print(f"{i+1}. {team}")
      choosen_index = int(input("Enter the number of the index team you want to select: ")) - 1
      User_team = team_names[choosen_index]
      User_team_data = df[df['Team'] == User_team]
      print(User_team_data)

    elif userinput=='30':
       ##only shows the unique team##
       for i, team in enumerate(team_names):
         print(f"{i+1}. {team}")




    elif userinput=='5':
      ## print the whole teams in ascending order of rank.
      print(df.sort_values((['Rank','Points']), ascending=True))


  ## Ask the user to input a keyword to display the value
 
       
       




   




           




    


## api workflow
Userinterface()


## components
## sort the list in an specific order 
#df.sort_values((['Rank','Points']), ascending=False)
## specify the conditon to find the specific one, rank 1 teams in the past decade
#rank1=df.loc[df['Rank']==1]
#print(rank1)
## iterate through each row
#for index, row in df.iterrows():  ## it list all team at same time, we can use this function to ask which team are they interested in.
#print(index,row ['Team'])

## the rank of arsenal is 3 , which means that permit us to allocate the specific location (R,C)
#print(df.iloc[3,4])

## access unique element
#print(df.head(4)[['Team','Games','Season']])

## use iloc function to modify the associated array
#df.iloc[3,1]

