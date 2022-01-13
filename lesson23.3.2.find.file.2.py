import os
import random


def find_file(cur_path, file_name):
    # print('\nпереходим в', cur_path)

    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        # print('    смотрим', path)
        if file_name in i_elem:
            ways.append(path)
            # return path
        if os.path.isdir(path):
            # print('это директория')
            find_file(path, file_name)
    if len(ways) != 0:
        return ways
    else:
        return None


ways = list()
# dir_name = input('Ищем в директории: ')
# dir_name = 'c:' + os.path.sep
dir_name ='c:\PycharmProjects'
# user_file_name = input('Имя файла: : ')
user_file_name = 'lesson'
print(os.path.abspath(dir_name), user_file_name)
file_path = find_file(os.path.abspath(dir_name), user_file_name)
if file_path:
    print('\nНайдены следующие пути:')
    [print('   ', i_elem) for i_elem in file_path]
    random_file = file_path[random.randint(0, len(file_path)-1)]
    print('\nТекст файла {}:'.format(random_file))
    file1 = open(random_file, 'r', encoding='utf-8')
    for i_line in file1:
        print(i_line, end='')
    file1.close()
else:
    print('\nФайл не найден')
