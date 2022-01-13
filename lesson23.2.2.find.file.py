import os


def find_file(cur_path, file_name):
    # print('\nпереходим в', cur_path)

    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        # print('    смотрим', path)
        if file_name in i_elem:
            ways.append(path)
        if os.path.isdir(path):
            # print('это директория')
            find_file(path, file_name)
    if ways:
        return ways
    else:
        return None


ways = list()
# dir_name = input('Ищем в директории: ')
# dir_name = 'c:' + os.path.sep
dir_name ='c:\PycharmProjects'
# user_file_name = input('Имя файла: : ')
user_file_name = 'lesson'
print('Program will try to find file "{}" in directory "{}"'.format(user_file_name, os.path.abspath(dir_name)))
file_path = find_file(os.path.abspath(dir_name), user_file_name)
if file_path:
    print('\nResults:')
    [print('   ', i_elem) for i_elem in file_path]
else:
    print('\nFile not found')
