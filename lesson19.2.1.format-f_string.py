user_name = input('Введите пользователя: ')
file_name = input('Введите имя файла: ')

path = 'C:/{user}/docs/folder/{new_file}.txt'.format(
    user=user_name,
    new_file=file_name
)

path_2 = 'C:/{0}/docs/{0}/folder/{1}.txt'.format(
    user_name,
    file_name
)

path_3 = f'C:/{user_name}/docs/folder/{file_name}.txt'

print('Путь к файлу:', path)
print('Путь к файлу:', path_2)
print('Путь к файлу:', path_3)
