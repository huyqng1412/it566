class number_series():
    def series():
        total = 0.0
        print("Please enter some numbers: ")

        while True:
            # Normal string input
            user_input = input("> ")
            
            if user_input in ['q', 'quit']:
                print("Bye!")
                break
           

            try: 
                # split() separated inputs by spaces
                string_numbers = user_input.split()
                # map() turns the inputs to float or int
                series_of_numbers = map(float, string_numbers)
                # list() puts all the entered numbers inside a list
                list_of_numbers = list(series_of_numbers)

                average = sum(list_of_numbers)/len(list_of_numbers)
                total = sum(list_of_numbers)

                print(f'Number entered: ', len(list_of_numbers))
                print(f"The sum of the numbers entered: ",total) 
                print(f'The average of the numbers entered: ', average)
            except ValueError:
                print("Invalid inputs!")
                return
