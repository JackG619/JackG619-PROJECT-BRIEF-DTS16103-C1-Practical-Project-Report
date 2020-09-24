# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 17:04:34 2020

@author: Jack Goggin
"""

import pandas as pd
# imports the pandas library
# assigns it to the word 'pd', as this is shorter it saves time because we don't have to write 'pandas' each time
# we use this module, instead just write 'pd'
import matplotlib.pyplot as plt
# imports the matplotlib.pyplot library and assigns to plt
# used this module for display graphs about data
import math
# imported to use pi

def menu():
    print("\n\n ---------------- THIS IS THE FIFA 19 VANGUARD HUB ---------------- \n\n")
    print(" 1. Search the database for a player's correct name\n 2. Get their in-game stats\n 3. Get the player information\n 4. Get career mode information\n 5. Display categories of in-game stats as a radar chart\n")
    loop = True
    while loop is True:
        # this will loop asking the user for a number, which decides what section the user goes to, until the user enters a valid entry
        # essentially if the user inputs a number, an error will not be returned, so it will not loop
        # if anything other than an integer is entered, like a string, an error will be returned and the 'except' code will run
        try:
            # tries this code until the user enters a valid entry
            choice = (int(input("Enter a number for what you want to do: ")))
            # specifies an integer must be inputted
            
            while choice not in [1, 2, 3, 4, 5, 6]:
                # will loop asking for a number if the user enters a number not in this array
                print("\n !!!! It must be a number between 1 - 6 !!!!")
                choice = (int(input("Enter your decision: ")))
            
            # the choice entry decides which function is called
            # if the user inputs 1, the function will be called to search the database and that code will be executed
            if choice == 1:
                loop = False
                # loop is set to False, so that the original while loop will not iterate again
                # without this, after the function that has been called is completed, this would be looped through again as the value would still be true
                search_database()
            elif choice == 2:
                loop = False
                get_player_stats()
            elif choice == 3:
                loop = False
                get_ingame_stats()
            elif choice == 4:
                loop = False
                get_player_info()
            elif choice == 5:
                loop = False
                get_career_mode_info()
            elif choice == 6:
                loop = False
                radar_chart_stats()
        except:
            # if input for choice returns an error this will be called
            # then the while loop will loop again
            print("\n !!!! You must input a number from the list !!!! ")

    
def intro():
    # defines the function for the introduction of the user
    # decompostion - break down big problems into smaller problems. Smaller problems easier to solve, re-construct to solve big problem
    # good to use decomposition, as makes code more readable, easier to troubleshoot and the function can be re-used elsewhere
    
    print("\n\nHello and welcome to the FIFA 19 vanguard - a database of players in FIFA 19")
    print("Search for your favourite players and see their statisitcs on the 2019 edition of the game")
    print("But that's not all! With this technology you can compare players stats - shooting, defending, potential in career mode, height; compare it all!")
    print("Search for that perfect player to make your team click? Search via specific parameters to find that player! ")
    print("E.g. Over 6ft, more than 80 pace, more than 84 defending, high defensive work rate. Find the players that match your needs! ")
    print("\n\nThere are 92 different types of statistic stored on each player: \n\n")
    # display an introduction message to the user - explains what the application can do
    
    df = pd.read_csv('fifa_cleaned.csv')
    # 'df' is short for data frame. A dataframe, part of the pandas library, is a "2D tabular data structure"
    # "data is aligned in a tabular fashion in rows and columns"..."three principal components, the data, rows and columns"
    # https://www.geeksforgeeks.org/python-pandas-dataframe/
    # this line read the comma-seperated value (csv) file into a data frame, via the file name 'fifa_claned.csv'
    # this is saved in the same location as the file, otherwise we would have to specify the filepath
    # by using a dataframe, the information is more readable and easier to parse
    
    column_headers = df.columns.tolist()
    # df.columns gets the header of each column, this is stored as a 'numpy.ndarray'
    # .tolist() converts the columns from type 'numpy.ndarray' to a list type, making it easier to read and parse
        
    for counter, value in enumerate(column_headers, start = 1):
        print(counter, ' - ', value)
    # enumrate function adds a counter to the variable. So this would add a counter to each header in the table
    # the for loop iterates through the list generated by the enumerate function
    # the enumerate function splits the list into two values - a number (counter), and the header name
    # the for loop assings the variable name counter to the number and the value variable to the header name
    # then for each line as it loops, it prints the counter variable, followed by a string ' - ', then the value variable
    # which displays the "counter ' - ' header name" or "1 - id"
    
    menu()
    

def search_database():
    # this will be a fucntion that allows users to search for players in a database
    # this is needed as a player may search for Wilson, as in Callum Wilson, but there are multiple players with the last name Wilson
    # this will return each player with 'Wilson' in there name, allowing them to specify the correct player
    
    df = pd.read_csv('fifa_cleaned.csv')
    player_data = df['name']
    # converts data frame into a series that includes just the column with header 'name'
    print("Here you can search for stats belonging to a certain player")
    print("First we must make sure you are searching for the correct player")
    # explains what is needed before we search for the stats
    
    desired_player = (str(input("Input the player you want to search for: "))).capitalize()
    # gets a string input from the user to determine the player they want to search for
    # capitalize() is a function that capitalises the first letter, as each name in the dadtabase has a capital first letter, so this is needed to match properly
    list_of_players_found = []
    # defines a list of the players that will be found on the upcoming search on the users input
    for index, player_name in player_data.items():
    # iterates through the series, assigning the index the variable index and the data in the column 'name' to the variable 'player_name'
        if desired_player in player_name:
            # if statement, if the string that the user entered is contained in one of the values in the 'name' column
            # rather than use the "player_name = value", this function will check if the string is contained within
            # meaning players with similiar names, but no exact to the user input, can be found
            list_of_players_found.append(player_name)
            # if a name is found, it is added onto the list defined above
            # append adds to end, rather than overwriting

    if len(list_of_players_found) != 0:
        # if statement checks that list is not empty
        # a list of length 0 would mean it is empty, as there are no entries. A empty list would mean no players found
        print("\nPlayers found: \n")
        print('\n'.join(list_of_players_found))
        # this join() function, displays the list without the brackets, but seperates them but '\n' which leaves a line
        # makes it more readable and user friendly
    else:
        print("\nThis name was not found in the database")
        # prints no players found as the list length was zero
        
def get_player_stats():
    desired_player = (str(input("Enter a player's name to see their statistics: ")))
    pd.set_option('display.max_rows', None)
    player_stats_column = pd.read_csv('fifa_cleaned.csv', index_col='name')
    # this saves just the column 'name' to the 'player_stats' variable. This means just the player names
    player_stats = player_stats_column.loc[desired_player]
    # .loc method accesses a group of rows and columns by a label. Previously defined just the 'name' column. This allows us to search by 'name'
    # so we pass a parameter, say 'L. Messi' this searches the previous data frame that stores just the player names column
    # .loc will then access all data belonging to 'L.Messi' name. We then print this data. Assigns this to the 'player_stats' column
    print("\n")
    # print empty line to make displayed data more readable
    for index, value in player_stats.items():
        # iterates through the panda series 'player_stats'. Assigns the index column to the variable index and the corresponding statistic to the variable value
        print(f"{index} - {value}")
        # f string format
        # curly brackets represent what will be replaced. In this case index and value variables are placed in the string within the curly brackets
        # this function iterates through each index and corresponding value, prints the value followed by the dash followed by the statistic

def get_ingame_stats():
    while True:
        try:
            desired_player = (str(input("Input the player you want to search for: ")))
            if desired_player == "EXIT":
                break
            player_stats_column = pd.read_csv('fifa_cleaned.csv', index_col='name')
            player_stats = player_stats_column.loc[desired_player]
            ingame_stats = player_stats[['crossing', 'finishing', 'heading_accuracy', 'short_passing', 'volleys', 'dribbling', 'curve', 'freekick_accuracy', 'long_passing', 'ball_control', 'acceleration', 'sprint_speed', 'agility', 'reactions', 'balance', 'shot_power', 'jumping', 'stamina', 'strength', 'long_shots', 'aggression', 'interceptions', 'positioning', 'vision', 'penalties', 'composure', 'marking', 'standing_tackle', 'GK_diving', 'GK_handling', 'GK_kicking', 'GK_positioning', 'GK_reflexes']] 
            print("\nHere are the statistics for '" + desired_player + "': \n")
            for index, value in ingame_stats.items():
                print(f"{index} - {value}")
            break
        except:
            print("\nThat was no valid player name. It must be the player's exact name.")
            print("Try again or enter 'EXIT' to stop the application.")         
    
def get_player_info():
    while True:
        try:
            desired_player = (str(input("Input the player you want to search for: ")))
            if desired_player == "EXIT":
                break
            player_stats_column = pd.read_csv('fifa_cleaned.csv', index_col='name')
            player_stats = player_stats_column.loc[desired_player]
            ingame_stats = player_stats[['birth_date', 'age', 'height_cm', 'weight_kgs', 'positions', 'nationality', 'overall_rating', 'potential', 'preferred_foot', 'international_reputation(1-5)', 'weak_foot(1-5)', 'skill_moves(1-5)', 'work_rate', 'body_type', 'tags', 'traits']] 
            print("\nHere is the player information for '" + desired_player + "': \n")
            for index, value in ingame_stats.items():
                print(f"{index} - {value}")
            break
        except:
            print("\nThat was no valid player name. It must be the player's exact name.")
            print("Try again or enter 'EXIT' to stop the application.")        

def get_career_mode_info():
    while True:
        try:
            desired_player = (str(input("Input the player you want to search for: ")))
            if desired_player == "EXIT":
                break
            player_stats_column = pd.read_csv('fifa_cleaned.csv', index_col='name')
            player_stats = player_stats_column.loc[desired_player]
            ingame_stats = player_stats[['full_name', 'positions', 'nationality', 'overall_rating', 'potential', 'value_euro', 'wage_euro', 'release_clause_euro', 'club_team', 'club_rating', 'club_position', 'club_jersey_number', 'club_join_date', 'contract_end_year', 'national_team', 'national_rating', 'national_team_position', 'national_jersey_number', 'LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW', 'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM', 'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB' ]] 
            print("\nHere is the career mode information for '" + desired_player + "': \n")
            for index, value in ingame_stats.items():
                print(f"{index} - {value}")
            break
        except:
            print("\nThat was no valid player name. It must be the player's exact name.")
            print("Try again or enter 'EXIT' to stop the application.")  


def radar_chart_stats():
    exit_choice=False
    print("\n\n")
    # referenced later in this function to decide whether the user wants to exit
    while True:
        try:
            desired_player = (str(input("\nInput the player you want to search for: ")))
            if desired_player.upper() == "EXIT":
                break
            player_stats_column = pd.read_csv('fifa_cleaned.csv', index_col='name')
            player_stats = player_stats_column.loc[desired_player]
            pace = player_stats[['acceleration', 'sprint_speed']]
            shooting = player_stats[['positioning', 'finishing', 'shot_power', 'long_shots', 'volleys', 'penalties']]
            passing = player_stats[['vision', 'crossing', 'freekick_accuracy', 'short_passing', 'long_passing', 'curve']]
            dribbling = player_stats[['agility', 'balance', 'reactions', 'ball_control', 'dribbling', 'composure']]
            defending = player_stats[['interceptions', 'heading_accuracy', 'standing_tackle', 'sliding_tackle']]
            physicality = player_stats[['jumping', 'stamina', 'strength', 'aggression']]
            break
        except:
            print("\nThat was no valid player name. It must be the player's exact name.")
            print("Try again or enter 'EXIT' to stop the application.")

    def pace_stats(*args):
        # *args states that the function will receive an undefined amount of arguments
        
        #display radar chart of specific values - this one is pace
        pace_categories = ['acceleration', 'sprint_speed']
        # array defined here, this will act as the labels for the radar chart
        N = len(pace_categories)
        # the length of this array signals how many labels/values will be on the chart
        values_of_categories = []
        # empty array defined, which will later be filled with the values corresponding to each label
        for index, value in pace.items():
                    values_of_categories.append(value)
        # for loop, iterates through the panda series assigned to each category
        # so in this case iterates through the pace variable, .items() returns a tuple of the index and value in the series
        # for loop assigns it to the variables
        # each value, so each statistic, will be appended to the previously defined empty list
        # making a list of each statistic in this category for the specified player
        values_of_categories += values_of_categories[:1]
        # this appends the first value onto the end of the list, so that it completes the circle
        
        angles = [n / float(N) * 2 * math.pi for n in range(N)]
        angles += angles[:1]
        # what will be the angle of each axis in the plot? (we divide the plot / number of variable)
        # this determines the angle between each value, which is of course dependent on how many values we are making it with
        # adds this to a list, and finishes the list with the same value to complete the circle as before
        
        plt.polar(angles, values_of_categories)
        # plots the points on the graph
        plt.fill(angles, values_of_categories, alpha=0.3)
        # color the area inside the polygon
        plt.xticks(angles[:-1], pace_categories)
        # gives the graph the correct labels at each point
        
        #ax.set_rlabel_position(0)
        plt.yticks([25, 50, 76,], color = "black", size = 7)
        # sets labels for each circle, the color of text and the size of the text
        plt.ylim(0,100)
        # says the values must have a minimum of 0 and maximum of 100
        
        plt.show()
        # displays the graph
        
        # websites used to gain knowledge of how to create this graph:
            # - https://medium.com/python-in-plain-english/radar-chart-basics-with-pythons-matplotlib-ba9e002ddbcd
            # - https://python-graph-gallery.com/390-basic-radar-chart/
    
    
    def shooting_stats(*args):
        # display radar chart of specific values - this one is pace
        shooting_categories = ['positioning', 'finishing', 'shot_power', 'long_shots', 'volleys', 'penalties']
        N = len(shooting_categories)
        values_of_categories = []
        for index, value in shooting.items():
                    values_of_categories.append(value)
        values_of_categories += values_of_categories[:1]
        
        angles = [n / float(N) * 2 * math.pi for n in range(N)]
        angles += angles[:1]
        
        plt.polar(angles, values_of_categories)
        # color the area inside the polygon
        plt.fill(angles, values_of_categories, alpha=0.3)
        
        plt.xticks(angles[:-1], shooting_categories)
        
        #ax.set_rlabel_position(0)
        plt.yticks([25, 50, 76,], color = "black", size = 7)
        plt.ylim(0,100)
        
        plt.show()
        #print(shooting_categories)
        #print(values_of_categories)
    
    def passing_stats(*args):
        # display radar chart of specific values - this one is pace
        passing_categories = ['vision', 'crossing', 'freekick_accuracy', 'short_passing', 'long_passing', 'curve']
        N = len(passing_categories)
        values_of_categories = []
        for index, value in passing.items():
                    values_of_categories.append(value)
        values_of_categories += values_of_categories[:1]
        
        angles = [n / float(N) * 2 * math.pi for n in range(N)]
        angles += angles[:1]
        
        plt.polar(angles, values_of_categories)
        # color the area inside the polygon
        plt.fill(angles, values_of_categories, alpha=0.3)
        
        plt.xticks(angles[:-1], passing_categories)
        
        #ax.set_rlabel_position(0)
        plt.yticks([25, 50, 76,], color = "black", size = 7)
        plt.ylim(0,100)
        
        plt.show()
        #print(shooting_categories)
        #print(values_of_categories)
    
    def dribbling_stats(*args):
        # display radar chart of specific values - this one is pace
        dribbling_categories = ['agility', 'balance', 'reactions', 'ball_control', 'dribbling', 'composure']
        N = len(dribbling_categories)
        values_of_categories = []
        for index, value in dribbling.items():
                    values_of_categories.append(value)
        values_of_categories += values_of_categories[:1]
        
        angles = [n / float(N) * 2 * math.pi for n in range(N)]
        angles += angles[:1]
        
        plt.polar(angles, values_of_categories)
        # color the area inside the polygon
        plt.fill(angles, values_of_categories, alpha=0.3)
        
        plt.xticks(angles[:-1], dribbling_categories)
        
        #ax.set_rlabel_position(0)
        plt.yticks([25, 50, 76,], color = "black", size = 7)
        plt.ylim(0,100)
        
        plt.show()
        #print(shooting_categories)
        #print(values_of_categories)
    
    def defending_stats(*args):
        # display radar chart of specific values - this one is pace
        defending_categories = ['interceptions', 'heading_accuracy', 'standing_tackle', 'sliding_tackle']
        N = len(defending_categories)
        values_of_categories = []
        for index, value in defending.items():
                    values_of_categories.append(value)
        values_of_categories += values_of_categories[:1]
        
        angles = [n / float(N) * 2 * math.pi for n in range(N)]
        angles += angles[:1]
        
        plt.polar(angles, values_of_categories)
        # color the area inside the polygon
        plt.fill(angles, values_of_categories, alpha=0.3)
        
        plt.xticks(angles[:-1], defending_categories)
        
        #ax.set_rlabel_position(0)
        plt.yticks([25, 50, 76,], color = "black", size = 7)
        plt.ylim(0,100)
        
        plt.show()
        #print(shooting_categories)
        #print(values_of_categories)
    
    def physicality_stats(*args):
        # display radar chart of specific values - this one is pace
        physicality_categories = ['jumping', 'stamina', 'strength', 'aggression']
        N = len(physicality_categories)
        values_of_categories = []
        for index, value in physicality.items():
                    values_of_categories.append(value)
        values_of_categories += values_of_categories[:1]
        
        angles = [n / float(N) * 2 * math.pi for n in range(N)]
        angles += angles[:1]
        
        plt.polar(angles, values_of_categories)
        # color the area inside the polygon
        plt.fill(angles, values_of_categories, alpha=0.3)
        
        plt.xticks(angles[:-1], physicality_categories)
        
        #ax.set_rlabel_position(0)
        plt.yticks([25, 50, 76,], color = "black", size = 7)
        plt.ylim(0,100)
        
        plt.show()
        #print(shooting_categories)
        #print(values_of_categories)
    
    # radar chart code retrieved from https://medium.com/python-in-plain-english/radar-chart-basics-with-pythons-matplotlib-ba9e002ddbcd

    
    if desired_player.upper() != "EXIT":
        print("\nThese are the categories to choose from: \n - pace\n - shooting\n - passing\n - dribbling\n - defending\n - physicality")
        category_choice = (str(input("Input the category of statistics you want to search for: ")))    
        while category_choice.lower() not in ["pace", "shooting", "passing", "dribbling", "defending", "physicality", "exit"]:
            print("It must be one of these categories: \n - pace\n - shooting\n - passing\n - dribbling\n - defending\n - physicality")
            category_choice = (str(input("Input the category of statistics you want to search for: "))) 
        
        if category_choice.lower() == "pace":
            pace_stats(desired_player, player_stats, pace)
        elif category_choice.lower() == "shooting":
            shooting_stats(desired_player, player_stats, pace)
        elif category_choice.lower() == "passing":
            passing_stats(desired_player, player_stats, pace)
        elif category_choice.lower() == "dribbling":
            dribbling_stats(desired_player, player_stats, pace)
        elif category_choice.lower() == "defending":
            defending_stats(desired_player, player_stats, pace)
        elif category_choice.lower() == "physicality":
            physicality_stats(desired_player, player_stats, pace)  
        else:
            exit_choice=True
            
        if exit_choice:
            print("\n\n -------------------------EXIT path chosen-------------------------")
            # if exit_choice variable is true (player chose to exit rather than choose category)
            # then this is displayed and application ends
        else:
            repeat_choice = input(str("Do you want to go again?\n - 'yes' to go again\n - 'no' to exit\n\n"))
            if repeat_choice.lower() == "yes":
                radar_chart_stats()
            else:
                print("\n\n -------------------------EXIT path chosen-------------------------")
            # if the player once to goes again by entering 'yes', recursion is applied
            # the function is called again, essentially starting again from scratch
            # if the player enters anything other than 'yes' the exit path is chosen and the application ends
    else:
        print("\n\n -------------------------EXIT path chosen-------------------------")
    # if the player enters something that is not equal to 'EXIT' after upper case has been applied then the application will get the statistics
    # if the player enters 'exit' after upper case has been applied the application will stop

        
intro()
# calls/executes the intro() function
"""menu()"""
# calls/executes the menu() function
""""search_database()"""
# calls/executes the search_database() function
"""get_player_stats()"""
# calls/executes the get_player_stats() function
""""get_ingame_stats()"""
# calls/executes the get_ingame_stats() function
"""get_player_info()"""
# calls/executes the get_player_info() function
""""get_career_mode_info()"""
# calls/executes the get_career_mode_info() function
"""radar_chart_stats()"""
