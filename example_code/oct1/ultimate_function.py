# Write a program that performs basic arithmetic 
# functions: addition, subtraction, multiplication, and 
# division. Prompt the user to enter an operation 
# symbol (+, -, *, /) followed by a number. 
# Display the running total after each user entry. 
# Continue prompting for user input 
# until the user enters ‘q’ for quit.

class UltimateFunction:
    def func():
        total = 0.0
        print("Enter a number and an operation symbol (+, -, *, /)!")

        while True:
            user_input = input("> ")

            if user_input == "q":
                print("Final total is: ", total)
                break
        

            try:
                operator, number = user_input.split()
                number = float(number)
                

                if operator == "+":
                    total += number
                    print("Current total is: ", total)
                elif operator == "-":
                    total -= number
                    print("Current total is: ", total)
                elif operator == "*":
                    total *= number
                    print("Current total is: ", total)
                elif operator == "/":
                    if number != 0:
                        total /= number
                        print("Current total is: ", total)
                    else:
                        print("Invalid! No zero for division please!")
                else:
                    print("Invalid operator! Please enter a valid operation symbol (+, -, *, /)")
                    continue
            except ValueError:
                print("Invalid input! Format must be: <operator> <number> (example: + 10)")

                 


                


