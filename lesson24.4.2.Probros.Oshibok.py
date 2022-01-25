names_list = []
while True:
    try:
        name = input('Insert the Name: ')
        if name.lower() == 'error':
            raise BaseException('You break the program')
        if not name.isalpha():
            raise TypeError
        names_list.append(name)
        if len(names_list) == 5:
            print('No more space')
            break
    except TypeError:
        print('What did you enter?')
    except BaseException:
        names_list = []
        print('You entered STOP-word')
        raise ValueError("Please, don't insert STOP-word!")

names_file = open('names.txt', 'w')
names_file.write('\n'.join(names_list))
names_file.close()
print("Program completed, recording completed")
