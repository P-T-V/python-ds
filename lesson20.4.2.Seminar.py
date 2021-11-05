import random


nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]

nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]

nums1_set = set(nums_1)
print('1-е множество:', nums1_set)
nums2_set = set(nums_2)
print('2-е множество:', nums2_set)

print('\nМинимальный элемент 1-го множества:', min(nums1_set))
print('Минимальный элемент 2-го множества:', min(nums2_set))

rand1 = random.randrange(100, 201)
rand2 = random.randrange(100, 201)
print('\nСлучайное число для 1-го множества:', rand1)
print('Случайное число для 2-го множества:', rand2)

nums1_set.pop()
nums1_set.add(rand1)
# print(nums1_set)
nums2_set.pop()
nums2_set.add(rand2)
# print(nums2_set)

print('\nОбъединение множеств:', nums1_set | nums2_set)
# print('\nОбъединение множеств:', nums1_set.union(nums2_set))
print('\nПересечение множеств:', nums1_set & nums2_set)
# print('\nПересечение множеств:', nums1_set.intersection(nums2_set))
print('\nЭлементы, входящие в nums_2, но не входящие в nums_1:', nums2_set - nums1_set)
# print('\nЭлементы, входящие в nums_2, но не входящие в nums_1:', nums2_set.difference(nums1_set))
