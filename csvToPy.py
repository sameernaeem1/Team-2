import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("Dataset.csv")


# get a list of all team names
team_names = df['Team'].unique().tolist()


## UI 
def Userinterface():
 while True:
    print("-----Premier League Season's 2009 to 2022-----")
    print()
    userinput= input("1:Display Teams\n2:Compare Teams\n3:Choose Team\nQ:Quit\nChoose an Option:")
    if userinput == '1':
        for i, team in enumerate(team_names):
         print(f"{i+1}. {team}")

    elif userinput=='2':
      for i, team in enumerate(team_names):
        print(f"{i+1}. {team}")
      try:   
          chosen_team_index1 = int(input("Enter the  number of the team you want to select:")) - 1
          chosen_team1 = team_names[chosen_team_index1]
          print(f"First Team Picked:{chosen_team1}")
          chosen_team_df1=df[df['Team'] == chosen_team1]
          chosen_team_index2 = int(input("Enter the number of the team you want to compare it with:")) - 1
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


      except IndexError:
        print("Index number should be smaller\nPlease restart the program again:")
        break
     
       
    elif userinput=='3':
     
       for i, team in enumerate(team_names):
         print(f"{i+1}. {team}")   
       try: 
         chosen_team_index = int(input("Enter the number of the team you want to select: ")) - 1
         chosen_team = team_names[chosen_team_index]
         print(f"Team Picked:{chosen_team}")
         chosen_team_df=df[df['Team'] == chosen_team]
         user_keyword=input("Enter a keyword to search for the component of the team:(eg Points, rank or wins)\n")
         chosen_columns=[col for col in chosen_team_df.columns if user_keyword.lower() in col.lower()]
         if chosen_columns=='Goals':
          a=chosen_team_df['Goals'].unique().valus.tolist()
          c=chosen_team_df['Season'].values.tolist()
         else:
             a=chosen_team_df[chosen_columns].values.tolist()
             c=chosen_team_df['Season'].values.tolist()
       except IndexError:
         print("Index number should be smaller\nPlease restart the program again:")
         break


       fig, ax = plt.subplots()
       ax.set_title(chosen_team,fontsize=14)
       ax.set_xlabel("Year",fontsize=12)
       ax.set_ylabel(user_keyword, fontsize=10)
       ax.plot(c,a,'mD:',label=chosen_team)
       ax.grid(True)

       ax.legend()
       plt.show()
    elif userinput=='q' or userinput=='Q':
       ## quit
       break


## api workflow
Userinterface() 