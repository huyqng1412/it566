#Write a program that repeatedly prompts the user to enter some text
# at the terminal and store the user’s input in a list. If the user enters the text “show”, print the
# contents of the list to the terminal. If the user enters the text “exit”, print the list to the terminal
# then exit the program.

def list():
    entries = []
    print("Enter anything to the list: ")

    while True:
        user_input = input()
    
        if user_input.lower() == "show":
            print("Current entries: ", entries)

        elif user_input.lower() == "exit":
            print("Final entries:", entries)
            break
        else:
            entries.append(user_input)

list()
