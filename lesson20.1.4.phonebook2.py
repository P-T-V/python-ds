phonebook_dict = dict()

while True:
    print('\nТекущие контакты на телефоне:')
    for i_name in phonebook_dict:
        print(i_name, phonebook_dict[i_name])
    name = input('\nВведите имя: ')
    if name in phonebook_dict:
        print('Ошибка: такое имя уже существует.')
    elif name != 'end':
        phonebook_dict[name] = input('Введите номер телефона: ')
    else:
        break
