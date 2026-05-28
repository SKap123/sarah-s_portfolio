#sarah
#movie
#gives a movie rating output based on age
#functions
def movie_ratings():
    agestring= input("Please enter your age: ")
    age = int(agestring)
    if (age >= 17):
        print ("you can watch any movie including R-rated")
    elif age >= 13 :
        print("you can watch PG-13, PG, and G movies")
    elif age > 0:
        print ("you can watch G rated movies and PG with caution")
#main
movie_ratings()
