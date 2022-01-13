import os


def find_file(cur_path, file_name):
    print('\nпереходим в', cur_path)

    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        print('    смотрим', path)
        if file_name == i_elem:
            return path
        if os.path.isdir(path):
            print('это директория')
            result = find_file(path, file_name)
            if result:
                break
    else:
        result = None

    return result


file_path = find_file(os.path.abspath(os.path.join('..', '..', 'Skillbox')),
                      'lesson23.2.0.1.findfile.py')
if file_path:
    print('Абсолютный путь к файлу:', file_path)
else:
    print('Файл не найден')
