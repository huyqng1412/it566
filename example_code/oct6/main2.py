def sentence():
    user_input1 = input("Do you want to meet a friend: ")
    if user_input1.upper() in ['Y', 'YES']:
        while True:
            user_input2 = input("Enter a name: ")
            if not isinstance(user_input2, str):
                print("Not a number bro! A name!")
            else:
                user_input3 = input("Enter a place: ")
                if not isinstance(user_input3, str):
                    print("Not a number bro! A place's name!")
                else:
                    print(f'{user_input2} is waiting for you at {user_input3}!')
                    user_input4 = input("Do you want them to buy you a drink? ")
                    if user_input4.upper() in ['Y', 'YES']:
                        print("What do you want to drink?")
                        user_input5 = str(input())
                        if not isinstance(user_input5, str):
                            print("Not a number bro! A drink's name!")
                        else:
                            print(f'{user_input2} bought a(n) {user_input5} for you!')                                
                    elif user_input4.upper() in ['N', 'NO']:
                        print("Have fun!")
            while True:
                user_input6 = input("Do you wanna do it again? ")
                if user_input6.upper() in ['Y', 'YES']:
                    break
                elif user_input6.upper() in ['N', 'NO']:
                    print("Bye!")
                    return
                else:
                    print("Invalid!")
    elif user_input1.upper() in ['N', 'NO']:
        print("Nevermind!")
        return


sentence()

                    


   