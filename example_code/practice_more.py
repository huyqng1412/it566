def main():
    string_variable = "Hello World"
    print("Hello World!")
    print(f" First Letter: {string_variable[0]}" )

    hello = ['H', 'E', 'L', 'L', 'O']
    world = ['W', 'O', 'R', 'L', 'D']

    hello_world =f'{hello}{world}'

    for i in hello_world:
        print(f'{i}', end='')
    print() # Add a newline for cleaner output
    
    for i in hello:
        print(f'{i}', end='')
    print()
    
    for i in world:
        print(f'{i}', end='')
    print()
def people():
    numbers = []

    for i in range(20):
        numbers.append(i)
    print(f'{numbers}')

    for i in numbers:
        print(f'{i}', end=' ')


if __name__ == '__main__':
    main()
    people()
    