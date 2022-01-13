import os


def print_dirs(project):
    print('\nСодержимое директории:', project)
    for i_elem in os.listdir(project):
        path = os.path.join(project, i_elem)
        # print(os.path.relpath(i_elem))
        print('    ', path)


def find_dir(folder, start_way=os.path.abspath(os.path.sep)):
    if folder in os.listdir():
        # print('Содержание папки "access":', os.listdir('access'))
        if os.path.exists(os.path.join(os.path.abspath('access'), 'admin.bat')):
            abs_way = os.path.join(os.path.abspath('access'), 'admin.bat')
            print(abs_way)
            return abs_way
    # for i_elem in start_way:
    if os.path.isdir(start_way):
        os.chdir(start_way)
        for i_elem in os.listdir(start_way):
            new_way = os.path.abspath(i_elem)
            print(new_way)
            find_dir(folder, new_way)


# find_dir('access')
# print(os.listdir())

print(os.path.abspath(os.listdir()[1]))
print('имя директории пути path:', os.path.dirname(os.path.abspath(os.listdir()[1])))
print(os.path.relpath(os.path.abspath(os.path.sep)))

projects_list = ['new', 'access', 'admin.bat']
path_to_bat = os.path.abspath(os.path.join(projects_list[0], projects_list[1], projects_list[2]))
print('\nАбсолютный путь до файла:', path_to_bat)
print('Относительный путь до файла: ', os.path.relpath(path_to_bat))

# way = find_dir('access')
# print('Абсолютный путь до файла:', way)


# if os.path.exists(os.listdir()[1]):
#     print(os.path.dirname(os.path.abspath(os.listdir()[1])))
#     path_to_project = os.path.dirname(os.path.abspath(os.listdir()[1]))
# print_dirs(path_to_project)
path_to_project = os.path.abspath(os.path.join('..', '..', 'Skillbox'))
print('\nПуть к папке Skillbox:', path_to_project)
print_dirs(path_to_project)

print('\nКорень диска:', os.path.abspath(os.path.sep))
