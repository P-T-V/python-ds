import os


folder_name = 'project'
file_name = 'my_file.txt'
real_path = os.path.join('docs', folder_name, file_name)
print(real_path)
abs_path = os.path.abspath(file_name)
print(abs_path)
print(os.path.abspath('new_folder'))
print(os.path.abspath('../new_folder'))  # Esli nujno v katalog na uroven vishe
print(os.path.abspath(os.path.join('..', 'new_folder')))  # Tak pravilnee
print(os.path.abspath('/new_folder')) #Srazu v koren diska
print(os.path.abspath(os.path.join(os.path.sep, 'new_folder')))  # Tak pravilnee - v koren diska
print(os.path.abspath(os.path.sep))


def print_dirs(project):
    print('\nСодержимое директории:', project)
    for i_elem in os.listdir(project):
        path = os.path.join(project, i_elem)
        print('    ', path)


projects_list = ['python-ds', 'Skillbox']
for i_project in projects_list:
    path_to_project = os.path.abspath(os.path.join('..', '..', i_project))
    print_dirs(path_to_project)