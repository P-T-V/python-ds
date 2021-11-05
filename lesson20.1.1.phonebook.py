# phonebook_list = [
#     ['Ваня', 88006663636],
#     ['Петя', 88005553535],
#     ['Лена', 88007773737]
# ]
#
# name = input('Введите имя: ')
#
# is_exist = False
# for i_person in phonebook_list:
#     if i_person[0] == name:
#         is_exist = True
#         print(i_person[1])
#         break
# if not is_exist:
#     print('Ошибка: человек с именем {0} не найден.'.format(name))

phonebook_dict = {
    'Ваня': 88006663636,
    'Петя': 88005553535,
    'Лена': 88007773737
}

name = input('Введите имя: ')

if name in phonebook_dict:
    print(phonebook_dict[name])
else:
    print('Ошибка: человек с именем {0} не найден.'.format(name))
