phonebook_dict = dict()
while True:
    phonebook_surname = input('\nВведите фамилию: ')
    if phonebook_surname == 'stop':
        break
    phonebook_name = input('Введите имя: ')
    if phonebook_name == 'stop':
        break
    if (phonebook_surname, phonebook_name) in phonebook_dict:
        print('Этот человек уже есть в словаре')
    else:
        phonebook_number = int(input('Введите номер телефона: '))
        phonebook_dict[phonebook_surname, phonebook_name] = phonebook_number
    print('\nТекущий словарь контактов:')
    print(phonebook_dict)
    # for i_person in phonebook_dict:
    #     print('Surname: {surname}, Name: {name}, Phone: {phone}'.format(
    #         surname=i_person[0],
    #         name=i_person[1],
    #         phone=phonebook_dict[i_person]
    #     ))
    # for i_person in phonebook_dict:
    #     i_surname, i_name = i_person
    #     print('Surname: {surname}, Name: {name}, Phone: {phone}'.format(
    #         surname=i_surname,
    #         name=i_name,
    #         phone=phonebook_dict.get(i_person)
    #     ))
    for i_person, i_phone in phonebook_dict.items():
        print('Surname: {surname}, Name: {name}, Phone: {phone}'.format(
            surname=i_person[0],
            name=i_person[1],
            phone=i_phone
        ))