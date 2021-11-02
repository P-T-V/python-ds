user_path = input('Введите путь к файлу: ')
user_disk = input('На каком диске должен лежать файл: ').upper()
file_ext = input('Требуемое расширение файла: ').lower()

if user_path.endswith(file_ext) and user_path.startswith(user_disk):
    print('Путь корректен!')
elif not user_path.endswith(file_ext):
    print('Ошибка: неверное расширение файла.')
elif not user_path.startswith(user_disk):
    print('Ошибка: неверно указан диск.')
