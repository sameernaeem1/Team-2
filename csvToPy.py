import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv("Dataset.csv")


# get a list of all team names
team_names = df['Team'].unique().tolist()


## UI 

def Userinterface():
 while True:
    userinput= input("choose the option\nq:Quit\n0:display the whole team in whole season\n1:display the status of each team in whole season\n2:display a team\n3:display team number\n4:compare another team with your choosen team\n5:display the asending order rank of each teams in whole seasons\n6:Search team and display the customised component\n7:display a team visualisation")
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
      print("Select a team:")
      for i, team in enumerate(team_names):
         print(f"{i+1}. {team}")
      selected_team_index = int(input("Enter the number of the team you want to select: ")) - 1
      selected_team = team_names[selected_team_index]
      selected_team_data = df[df['Team'] == selected_team]
      print(selected_team_data)

    elif userinput=='3':
       ##only shows the unique team##
       for i, team in enumerate(team_names):
         print(f"{i+1}. {team}")

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


  ## Ask the user to input a keyword to display the value
    elif userinput=='6':
       for i, team in enumerate(team_names):
         print(f"{i+1}. {team}")
       chosen_team_index = int(input("Enter the number of the team you want to select: ")) - 1
       chosen_team = team_names[chosen_team_index]
       print(f"Team:{chosen_team}")
       chosen_team_df=df[df['Team'] == chosen_team]
       user_keyword=input("Enter a keyword to search for the component of the team:(eg Points, rank or wins)")
       chosen_columns=[col for col in chosen_team_df.columns if user_keyword.lower() in col.lower()]
       print(chosen_team_df[chosen_columns])
       if  user_keyword =='wins':
        totalnum=chosen_team_df[chosen_columns].sum()
        print(f"{chosen_team}  get {totalnum} ")
       elif user_keyword=='rank':
        print(f"{chosen_team} got different {user_keyword} in different season for {len(chosen_team_df) } times")
       elif user_keyword=='points':
        totalpoints=chosen_team_df[chosen_columns].sum()
        print(f"{chosen_team} got total {totalpoints} points")


    elif userinput=='7':
     for i, team in enumerate(team_names):
        print(f"{i+1}.{team}")
     chosen_team_index = int(input("Enter the number of the team you want to select: ")) - 1
     chosen_team = team_names[chosen_team_index]
     print(f"Team:{chosen_team}")
     chosen_team_df=df[df['Team'] == chosen_team]
     user_keyword=input("Enter a keyword to search for the component of the team:(eg Points, rank or wins)")
     chosen_columns=[col for col in chosen_team_df.columns if user_keyword.lower() in col.lower()] 
     selected_comp=chosen_team_df[chosen_columns].iloc[0]
       ## 
     plt.bar(["comp1"],[selected_comp.values[0]])
     plt.title(f"{chosen_team} {user_keyword}")
     plt.show()
   
   
   



      
   
          

   

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