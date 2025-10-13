#Program Specification 2: Write a program that computes and 
# displays a running total of numbers entered by the user. 
# Allow the user to enter numbers with decimal points. 
# The program should run until the user enters “q” for quit.

class super_sum():
    def sum_up():
        total = 0.0
        print("Enter some numbers: ")

        while True:
            user_input = input("> ")

            if user_input.lower() == "q":
                print("The total is: ", total)
                print("Bye")
                break

            try:
                numbers = float(user_input)
                total += numbers
                print("Total is: ", total)
            except ValueError:
                print("Please enter an appropriate number!")
            
