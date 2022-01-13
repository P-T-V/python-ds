import os


path = 'C:\PycharmProjects\Skillbox\Lessons\lesson23.2.1.icons.py'
# path = input('Путь: ')
if os.path.isdir(path):
    print('это директория')
elif os.path.islink(path):
    print('это ссылка')
elif os.path.isfile(path):
    print('это файл')
    size = os.path.getsize(path)
    print('Размер файла: {} байт'.format(size))
else:
    print('Указанного пути не существует')
