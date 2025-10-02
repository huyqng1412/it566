# Write a program that reverses the text entered by the user at the
# terminal. Print the reversed text to the terminal. Continue prompting the user to enter text until
# the user types “exit”.
class UltimateReverse:
    def reverse():
        while True:
            user_input = input("Enter any text: ").strip()
            reverse_text = user_input[::-1]


            if not isinstance(user_input, str):
                print("Please enter a text, not a number!")
            else:
                print(f"You've entered: {user_input}. Let's reverse the text you entered:")
                print(reverse_text)
            while True:
                another = input("Do you want to try another text? ").strip()

                if another in ["yes", "Yes", "y"]:
                    break
                elif another in ["no", "No", "n"]:
                    print("Bye")
                    return
                else:
                    print("Invalid input.")



