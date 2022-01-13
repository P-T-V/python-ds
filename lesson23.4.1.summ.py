import os


path1 = os.path.join('d:', os.path.sep, 'task', 'numbers.txt')
path2 = os.path.join('d:', os.path.sep, 'task', 'answer.txt')
numbers_file = open(path1, 'r')
results_file = open(path2, 'w')
summ = 0
print('\nСодержимое файла {}:'.format(path1))
for i_line in numbers_file:
    print(i_line, end='')
    summ += int(i_line)
print()
results_file.write(str(summ))
results_file.close()
results_file = open(path2, 'r')
# results_file.write('\n')
print('\nСодержимое файла {}:'.format(path2))
print(results_file.read())
numbers_file.close()
results_file.close()
