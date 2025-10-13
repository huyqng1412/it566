#Program Specification 1: Write a program that repeatedly prompts the user to enter some text
# at the terminal and store the user’s input in a list. If the user enters the text “show”, print the
# contents of the list to the terminal. If the user enters the text “exit”, print the list to the terminal
# then exit the program.
class super_list():
    def ultimate_list():
        text_list = []
    

        while True:
            user_input = input("Enter something: ")

            if user_input.lower() == "show":
                print(f"Current entries: ", text_list)

            elif user_input.lower() == "exit":
                print(f"All entries: ", text_list)
                break
            else:
                text_list.append(user_input)

    
