nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
# список с 3мя уровнями: 1й (внешний) из 2х членов, 2й из 3х членов, 3й уровень (внутренний) также из 3х членов
nice_copy = []
[[[nice_copy.append(nice_list[i][j][k]) for k in range(3)] for j in range(3)] for i in range(2)]
print(nice_copy)

# Другой вариант решения:
# nice_copy2 = [num for num in list_2l for list_2l in nice_list] переставляем
# nice_copy2 = [num for list_2l in nice_list for num in list_2l]

# nice_copy2 = [num for num in list_3l for list_3l in list_2l for list_2l in nice_list] переставляем
nice_copy2 = [num for list_2l in nice_list for list_3l in list_2l for num in list_3l]

print(nice_copy2)
