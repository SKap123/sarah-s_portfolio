#plane_movie.py
#The purpose of this function is to help users find movie recommendations that are within their flight time...
# ...and genre as well as search for more facts about these movies.

#Initialize
#Imports pandas library and .csv file, creates arrays out of the .csv sections, and creates an array for filtering
import pandas as pd
data = pd.read_csv("IMDb_Movies_List.csv")
runtime = data["Runtime"].tolist()
genre = data["Genre"].tolist()
overview = data["Overview"].tolist()
movie_name = data["Series_Title"].tolist()
year = data["Released_Year"].tolist()
director = data["Director"].tolist()
star = data["Star1"].tolist()
rating = data["IMDB_Rating"].tolist()
filter = []

#Functions
#There are 3 main functions: the movie filter, the movie search, and the menu

#This function takes in user input about flight time and genre and outputs movie recommendations

#The function works by filtering the .csv file to find movies within the time constraints..
#..and that match the selected genre
def movie_filter(flight_time, topic):
    for i in range (len(runtime)):
        if flight_time > runtime[i] and topic in genre[i]:
            filter.append(movie_name[i])
    item_value = len(filter)
    #This section tests how many movies were found by the filter,
    # and matches the output to the length of the filter
    if item_value == 0:
        print(f"{item_value} movies were found. Sorry!")
        filter.clear()
    elif item_value < 2:
        print(f"{item_value} movie was found")
        print(f"We recommend watching {filter[0]}!")
        filter.clear()
    elif item_value < 3:
        print(f"{item_value} movies were found")
        print(f"We recommend watching {filter[0]}!")
        print(f"If you do not like that option, try {filter[1]}!")
        filter.clear()
    elif item_value < 4:
        print(f"{item_value} movies were found")
        print(f"We recommend watching {filter[0]}!")
        print(f"If you do not like that option, try {filter[1]} or {filter[2]}!")
        filter.clear()
    elif item_value >= 4:
        print(f"{item_value} movies were found")
        print(f"We recommend watching {filter[0]}!")
        print(f"If you do not like that option, try {filter[1]}, {filter[2]}, or {filter[3]}!")
        #Since this conditional statement catches all amounts of movies above 4,
        # we give the option to see all of the movies, not just the first four
        whole_list = input("Want to see the whole list? (yes/no): ")
        whole_list_lower = whole_list.lower()
        if whole_list_lower == "yes":
            print(f"""Here's all of the movies found!:
{filter}""")
            filter.clear()
        elif whole_list_lower == "no":
            print("No problem! We hope you like our recommendations!")
            filter.clear()
        #Catches any errors in input
        else:
            print("Please enter a valid input")
            filter.clear()


#This function takes in a user input of a movie name and outputs facts about that movie
def movie_search(name):
    not_found = "false"
    user_movie_title = name.title()
    for i in range (len(runtime)):
        if user_movie_title == movie_name[i]:
            filter.append(year[i])
            filter.append(runtime[i])
            filter.append(genre[i])
            filter.append(rating[i])
            filter.append(overview[i])
            filter.append(director[i])
            filter.append(star[i])
    #if no movies were found, "not_found" will be "true", triggering the print of "movie not found"
    if len(filter) == 0:
        not_found = "true"
    #if movies are found, the "not_found" will be "false", triggering the print of movie facts
    if not_found == "false":
        print(f"""Great movie choice! Here's some facts about {user_movie_title}:
Release year: {filter[0]}
Runtime: {filter[1]} minutes long
Genre: {filter[2]}
IMDb rating: {filter[3]}/10
Overview: {filter[4]}
Director: {filter[5]}
Star: {filter[6]}""")
        filter.clear()
    elif not_found == "true":
        print("Movie not found")
        print("Please enter a valid input")
        print(f"{user_movie_title}")
        filter.clear()

#the main function creates a user interface to access the movie functions
def menu():
    print ("-------------------------------------------------------")
    print("| Welcome to the In-Flight Movie Picker!              |")
    print("| Let’s help you find a movie to watch on your flight |")
    print ("-------------------------------------------------------")
    #while true loops the program until the user chooses to leave
    while True:
        print("============ Main Menu ============")
        print("Choose a function:")
        print("""-------
| Rec | - Find movie recommendations based on flight time and genre
-------
----------
| Search | - Find a movie recommendation you like? Learn facts about the movie here
----------
--------
| Quit | - Exits the program
--------""")
        #allows user to learn more about the functions then select one to use
        procedure_not_lower = input("Choose (rec, search, quit) >> ")
        procedure = procedure_not_lower.lower()
        #enters the movie recommender function
        if procedure == "rec":
            print("                                         ")
            print ("========= Movie Recommender =========")
            print("Great choice! Let's get you some movie suggestions!")
            print("---------------------------------------------------")
            #ensures that if they dont enter a number, the program does not crash (gains time as input)
            try:
                flight_time = int(input("How long is your flight, in minutes? (Just write the number): "))
            except:
                print("Please enter a number for your flight time. Returning to the menu.")
                continue
            #(gains genre as input)
            topic_not_lower = input("What is a genre of movies you like watching?: ")
            topic = topic_not_lower.lower()
            print("--------------------------------------------------")
            print("Thank you for the information! Here are the results of your search:")
            print(">>>>>>")
            #CALLS the movie recommender function with the variables that store the user input
            movie_filter(flight_time, topic)
            print ("=================================================")
            #Allows users to return to the menu when then are done viewing their results
            back_to_menu_not_lower= input("Type “menu” when you are ready to return to the menu (menu) >> ")
            back_to_menu = back_to_menu_not_lower.lower()
            if back_to_menu == "menu":
                continue
            else:
                print("Please enter a valid input. Returning to menu")
                continue
        #Enters the search function
        elif procedure == "search":
             print ("""
=========== Movie Search ===========""")
             print("Awesome. Let's find out some movie facts!")
             print("-----------------------------------------")
             movie_name = input("What is the name of the movie you want to learn more about?: ")
             print("-----------------------------------------------------------")
             print("Thanks for the info! Here are the results of your search: ")
             print(">>>>>>")
             #CALLS the movie search function
             movie_search(movie_name)
             print ("---------------------------------------------------------------------------------------")
             #Allows users to return to the menu when then are done viewing their results
             back_to_menu_not_lower_two= input("Type “menu” when you are ready to return to the menu (menu) >> ")
             back_to_menu_two = back_to_menu_not_lower_two.lower()
             if back_to_menu_two == "menu":
                 continue
             else:
                print("Please enter a valid input. Returning to menu")
                continue
        #Enters the quit procedure
        elif procedure == "quit":
            print("--------------------------------------------------------")
            print("| Thank you for using the In-Flight Movie Picker! Bye! |")
            print("--------------------------------------------------------")
            break
        #Catches errors in entering the code
        else:
            print("Please enter a valid function. Returning to menu.")
            continue

#Main
menu()

#Source for data set
#Website name: www.kaggle.com
#Author: Harshit Shankhdhar
#URL: https://tinyurl.com/34sfsvc2
#Article name: IMDB Dataset of Top 1000 Movies
#Date: not found
