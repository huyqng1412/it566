# Write a program that computes and displays a running total of numbers entered by the user. 
# Allow the user to enter numbers with decimal points. The program should run until the user enters “q” for quit.

def total_num():
    total = 0.0
    print("Enter a number (decimal is fine):")

    while True:
        user_input = input(">").strip()


        if user_input.lower() == "q":
            print(f"Total is: ", total)
            print("Bye")
            break


        try:
            numbers = float(user_input)
            total += numbers
            print("Total is: ", total)
        except ValueError:
            print("Idiot! Press 'q' to quit.")



        
total_num()