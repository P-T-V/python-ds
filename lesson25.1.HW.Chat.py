import time


user_name = input('What is your name? ')
while True:
    print('1. Chat history; 2. Write message')
    response = input('Enter 1 or 2: ')
    if response == '1':
        try:
            with open('chat.txt', 'r', encoding='utf-8') as file:
                messages = file.readlines()
                print(''.join(messages))
        except FileNotFoundError:
            print('Now chat history is empty.\n')
    elif response == '2':
        new_message = input('Enter your message: ')
        with open('chat.txt', 'a', encoding='utf-8') as file:
            file.write('{name}: {message}\n'.format(name=user_name, message = new_message))
    else:
        print('Unknown command')
