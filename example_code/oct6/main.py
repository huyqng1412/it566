def f(message:str):
    print(f'f(): {message}')


def main():
    keep_going = True
    user_input_list = []
    while keep_going:
        user_input = input("Enter something: ")
        
        if user_input.upper() in ['Q', 'QUIT', 'EXIT']:
            keep_going = False
        else:
            user_input_list.append(user_input)
    print(user_input_list)

main()