## Practice


def func():
    while True:
        credit = input("Please enter your credit card number: ")
        credit = credit.replace("-", "")
        credit = credit.replace(" ", "")
        if len(credit) == 16 and credit.isdigit():
            print(f"The last four digits of your card are: {credit[-4:]}")

            pin = input("Please enter your pin: ")
            if len(pin) == 4 and pin.isdigit():
                print(f"Pin number received.")
                sec_code = input("Please enter your CVV: ")
                if len(sec_code) == 3 and sec_code.isdigit():
                    print(f"Credit card ending in: {credit[-4:]}")
                    print(f"Pin number: {pin}")
                    print(f"CVV: {sec_code}")
                else:
                    print("Invalid CVV number.")
            else:
                print("Invalid PIN number, must be 4 digits.")
        else:
            print("Invalid credit card number. Please enter a 16-digit number.")
        while True:
            another = input("Would you like to add another credit card? ")
            if another in ["yes", "y"]:
                break  # Break inner loop to restart the outer loop
            elif another in ["no", "n"]:
                print("Thank you for using our service. Goodbye!")
                return # Exit the entire function to stop
            else:
                print("Invalid response. Please enter 'yes' or 'no'.")

    
func()