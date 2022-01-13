import os


cur_path = os.path.join('c:', os.path.sep, 'PycharmProjects', 'Skillbox', 'Lessons')
# cur_path = os.path.join('c:', os.path.sep, 'PycharmProjects', 'Skillbox')
path_res = os.path.join('d:', os.path.sep, 'task', 'scripts.txt')
results = open(path_res, 'w', encoding='utf-8')
for i_elem in os.listdir(cur_path):
    path = os.path.join(cur_path, i_elem)
    if os.path.isfile(path):
        cur_file = open(path, 'r', encoding='utf-8')
        results.write('File {}:'.format(path))
        results.write('\n\n')
        for j_elem in cur_file:
            results.write(j_elem)
        cur_file.close()
        results.write('\n')
        results.write(40 * '*')
        results.write('\n\n')
results.close()
