#Sarah Kaplan
# Dog Breed (CREATE TASK)
#The purpose of my program is to help users choose a dog breed that meets their needs.

#Initialize
import webbrowser
import pandas as pd
data = pd.read_csv("dog.csv")
min_weight = data["Minimum Weight"].tolist()
name = data["Name"].tolist()
temperament = data["Temperament"].tolist()
image = data["Image"].tolist()
bred_for = data["BredFor"].tolist()
filter = []

#Functions
def getDogSize(size):
    size_lower = size.lower()
    if size_lower == "tiny":
        for i in range (len(name)):
            if min_weight[i] <= 10:
                filter.append(name[i])
        print(f"I recommend the {filter[0]} breed if you want a {size} dog!")
        print(f"Here are some other opinions for {size} dogs: {filter[1:(len(filter))]}")
        filter.clear()
    elif size_lower == "small":
        for i in range (len(name)):
            if min_weight[i] >= 11 and min_weight[i] <= 25:
                filter.append(name[i])
        print(f"I recommend the {filter[0]} breed if you want a {size} dog!")
        print(f"Here are some other opinions for {size} dogs: {filter[1:(len(filter))]}")
        filter.clear()
    elif size_lower == "medium":
        for i in range (len(name)):
            if min_weight[i] >= 26 and min_weight[i] <= 60:
                filter.append(name[i])
        print(f"I recommend the {filter[0]} breed if you want a {size} dog!")
        print(f"Here are some other opinions for {size} dogs: {filter[1:(len(filter))]}")
        filter.clear()

    elif size_lower == "large":
        for i in range (len(name)):
            if min_weight[i] > 60:
                filter.append(name[i])
        print(f"I recommend the {filter[0]} breed if you want a {size} dog!")
        print(f"Here are some other opinions for {size} dogs: {filter[1:(len(filter))]}")
        filter.clear()

    else:
        print("please enter a valid size")
def dog_search_engine(breed_name):
    for i in range (len(min_weight)):
        if name[i] == breed_name:
            filter.append(i)
    try:
        print(f"The temperament of this dog can be described as {temperament[filter[0]]}")
        print(webbrowser.open(image[filter[0]]))
        filter.clear()
    except:
        print("breed not found")
        filter.clear()

def bred_for_search(purpose):
    for i in range (len(name)):
        if purpose in bred_for[i]:
            filter.append(name[i])
    try:
        print(f"The {filter[0]} breed matches for the purpose of {purpose}")
        filter.clear()
    except:
        print("No breed match found")
        filter.clear()

def menu():
    print("Welcome to the dog breed finder!")
    while True:
        print("""You may choose to use any of our search funtions! Here are your options:
Dog Size Finder - input a size of dog you want and we will give you a matching recommendation!
Dog Traits Finder - input the name of a dog and find out about its temperament and looks
Dog Purpose Finder - input what you want the dog to be bred for and we will give you a matching recommendation""")
        q_one = input("What search function would you like to use? (size, trait, purpose): ")
        if q_one == "size":
            input_size = input("What size of dog are you looking for? (tiny, small, medium, large): ")
            getDogSize(input_size)
            leave_one = input("Would you like to continue? (yes, no): ")
            if leave_one == "yes":
                continue
            if leave_one == "no":
                break
            else:
                print("please enter a valid input")
                continue
        elif q_one == "trait":
            input_trait = input("What is the name of the dog you are looking for?: ")
            dog_search_engine(input_trait)
            leave_two = input("Would you like to continue? (yes, no): ")
            if leave_two == "yes":
                continue
            if leave_two == "no":
                break
            else:
                print("please enter a valid input")
                continue
        elif q_one == "purpose":
            input_purpose = input("What is the purpose you are looking for in a dog?: ")
            bred_for_search(input_purpose)
            leave_three = input("Would you like to continue? (yes, no): ")
            if leave_three == "yes":
                continue
            elif leave_three == "no":
                break
            else:
                print("please enter a valid input")
                continue
        else:
            print("Please enter a valid input")
            continue
#Main
#getDogSize("small")
#dog_traits_search("BostonTerrier")
#bred_for_search("Hunting")
menu()

#Sources
#Dog Dataset
#Website Name: Code.org
#URL: https://code.org/en-US
#Dataset Source:https://thedogapi.com/en
