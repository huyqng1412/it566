class super_reverse():
    def reverse():
        while True:
            print("Enter something: ")
            user_input = input().strip()
            reverse_text = user_input[::-1]

            if not isinstance(user_input, str):
                    print("Please enter texts, not numbers!")

            else:
                print(f"You have entered {user_input}, the reversed text of that is: ")
                print(reverse_text)

            while True:
                another = input("Do you want to enter another text? ")

                if another in ['y', 'Y', 'yes']:
                    break
                elif another in ['n', 'no', 'N']:
                    print("Bye")
                    return
                else:
                    print("Invalid")


            



        