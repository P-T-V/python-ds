import os


path1 = os.path.join('d:', os.path.sep, 'task', 'group_1.txt')
path2 = os.path.join('d:', os.path.sep, 'task', 'Additional_info', 'group_2.txt')
file1 = open(path1, 'r', encoding='utf-8')
file2 = open(path2, 'r', encoding='utf-8')
summa = 0
diff = 0
compose = 1

for i_line in file1:
    info = i_line.split()
    summa += int(info[2])
    diff -= int(info[2])
    # print(info, summa, diff)


for i_line in file2:
    info = i_line.split()
    compose *= int(info[2])
    # print(info, compose)


print(summa)
print(diff)
print(compose)

file1.close()
file2.close()
