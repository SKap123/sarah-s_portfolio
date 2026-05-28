#Sarah
#todo.py
#creates a functioning todo list for users packing clothes before a trip
#init
#functions
def todo():
    print("Welcome to the ultimate clothes packing list!")
    task = ["4 shirts", "3 pants", "2 layers", "6 pairs of socks", "4 PJs", "2-3 shoes", "formal wear", "accessories"]
    done = []
    while True:
        action = input("""Choose one of the following actions to continue:
    Add
    Mark as done
    Remove / clear
    Exit
Enter choice: """)
        action = action.lower()
#adding function
        if action == "add":
            add = input("What item would you like to add to the list?: ")
            if add == "":
                print ("Please enter a valid input. Returning to menu.")
                continue
            task.append(add)
            print (f"""You have added {add} to the list.
    tasks left: {task}
    tasks done: {done}""")
            continue
#mark as done function
        elif action == "mark as done":
            print(f"""You still need to do:
        {task}""")
            complete = input("What task have you completed?: ")
            if complete == "":
                print ("Please enter a valid input. Returning to menu.")
                continue
            try:
                task.remove(complete)
                done.append(complete)
                print (f"""Congrats! You marked {complete} as done.
    tasks left: {task}
    tasks done: {done}""")
                continue
            except:
                print("Please enter a valid input. Returning to menu.")
                continue
#remove / clear functions
        elif action == "remove / clear":
            choice = input("Would you like to remove one task or clear the whole list?(remove, clear): ")
            if choice == "":
                print ("Please enter a valid input. Returning to menu.")
                continue
            choice.lower
            #if they choose remove
            if choice == "remove":
                print(f"""You still need to do:
    {task}""")
                rem = input("What task would you like to remove?: ")
                if rem == "":
                    print ("Please enter a valid input. Returning to menu.")
                    continue
                try:
                    task.remove(rem)
                    print (f"""You removed {rem} from the list.
    tasks left: {task}
    tasks done: {done}""")
                    continue
                except:
                    print("Task to remove not in list. Returning to menu")
                    continue
            #if they choose clear
            elif choice == "clear":
                task.clear()
                print (f"""You cleared the list.
    tasks left: {task}
    tasks done: {done}""")
                continue
            else:
                print("Please enter a valid input. Returing to menu.")
                continue
#exit function
        elif action == "exit":
            print("Thanks for using the todo list! Happy travels.")
            break
#if menu choice is typed wrong
        else:
            print("Please enter a valid input. Returning to menu.")
            continue


#main
todo()
