#sarah
#madlibs
#asks user for input and provides a story from it
#init
import random
#functions
def madlibs():
    #gather input
    print("Welcome to madlibs!")
    place1 = input("Please enter a place to start or type random: ")
    if place1 == "random":
        rand0 = ["Chicago", "Boston", "Hawaii", "Greenland"]
        select0 = random.randint(0,3)
        place1 = rand0[select0]
    name1= input("Enter a name or type random: ")
    if name1 == "random":
        rand1 = ["Billy", "John", "Sally", "Ronald"]
        select1 = random.randint(0,3)
        name1 = rand1[select1]
    animal1= input("Enter an animal or type random: ")
    if animal1 == "random":
        rand2 = ["elephant", "seal", "whale", "tiger"]
        select2 = random.randint(0,3)
        animal1 = rand2[select2]
    adj1= input("Enter an adjective or type random: ")
    if adj1 == "random":
        rand3 = ["wacky", "goofy", "cruncy", "glittery"]
        select3 = random.randint(0,3)
        adj1 = rand3[select3]
    car1= input("Enter a vehicle or type random: ")
    if car1 == "random":
        rand4 = ["train", "speed boat", "unicycle", "skateboard"]
        select4 = random.randint(0,3)
        car1 = rand4[select4]
    adj2= input("Enter an adjective or type random: ")
    if adj2 == "random":
        rand5 = ["slippery", "bubbly", "hyper", "colorful"]
        select5 = random.randint(0,3)
        adj2 = rand5[select5]
    animal2= input("Enter an animal or type random: ")
    if animal2 == "random":
        rand6 = ["cat", "lion", "polar bear", "fish"]
        select6 = random.randint(0,3)
        animal2 = rand6[select6]
    verb1 = input("Enter a verb ending in -ing or type random: ")
    if verb1 == "random":
        rand7 = ["writing", "freezing", "screaming", "jumping"]
        select7 = random.randint(0,3)
        verb1 = rand7[select7]
    num1= input("Enter a number or type random: ")
    if num1 == "random":
        rand8 = [87, 100, 321, 25]
        select8 = random.randint(0,3)
        num1 = rand8[select8]
    noun1 = input("Enter a noun or type random: ")
    if noun1 == "random":
        rand9 = ["boot", "security camera", "tree", "air conditioner"]
        select9 = random.randint(0,3)
        noun1 = rand9[select9]
    food1= input("Enter a plural food: ")
    if food1 == "random":
        rand10 = ["pasta", "burgers", "icecream", "soup"]
        select10 = random.randint(0,3)
        food1 = rand10[select10]
    verb2 = input("Enter a verb or type random: ")
    if verb2 == "random":
        rand11 = ["fly", "cry", "think", "yodel"]
        select11 = random.randint(0,3)
        verb2 = rand11[select11]
    action = input ("Enter a past tense verb or type random: ")
    if action == "random":
        rand12 = ["took", "talked to", "jumped over", "spun"]
        select12 = random.randint(0,3)
        action = rand12[select12]
    num2= input("Enter a number or type random: ")
    if num2 == "random":
        rand13 = [40, 3, 24, 0]
        select13 = random.randint(0,3)
        num2 = rand13[select13]
    name2= input("Enter a name or type random: ")
    if name2 == "random":
        rand14 = ["jimmy", "bobby", "sandy", "olive"]
        select14 = random.randint(0,3)
        name2 = rand14[select14]

    print(f"""During my time at the University of \033[1m{place1.upper()} \033[0m, my roommate  \033[1m{name1.upper()} \033[0m was determined to get a pet  \033[1m{animal1.upper()} \033[0m.
There was a  \033[1m{adj1.upper()} \033[0m pet store nearby, so we took the  \033[1m{car1.upper()} \033[0m to go check it out.
When we walked in, I first noticed the  \033[1m{adj2.upper()} \033[0m  \033[1m{animal2.upper()} \033[0m staring at me in the corner. I immediately started  \033[1m{verb1.upper()} \033[0m.
Nonetheless,  \033[1m{name1.upper()}\033[0m said we had to keep going to find their  \033[1m{adj2.upper()} \033[0m  \033[1m{animal1.upper()} \033[0m. After  \033[1m{num1} \033[0m hours of looking around, we found it.
The \033[1m{animal1.upper()}\033[0m was playing with a \033[1m{noun1.upper()} \033[0m. “Aww look, now it's eating a bowl of \033[1m{food1.upper()} \033[0m!” said  \033[1m{name1.upper()} \033[0m.
I told  \033[1m{name1.upper()} \033[0m I had to get back to the dorm soon because I had to  \033[1m{verb2.upper()} \033[0m.
They quickly  \033[1m{action.upper()} \033[0m the  \033[1m{animal1.upper()} \033[0m and bought it for only  \033[1m{num2} \033[0m dollars.
My roommate decided the  \033[1m{animal1.upper()} \033[0m's name would be  \033[1m{name2.upper()} \033[0m.""")
#main
madlibs()
