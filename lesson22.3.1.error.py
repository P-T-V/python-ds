# Суть кода в том, что у вас есть общий словарь из нескольких ключей, значения которых равны ранее
# объявленным переменным. Затем вызывается функция, которая должна изменять значения словаря, добавляя к значениям
# случайное число, в зависимости от типа данных. Но при этом меняются и ранее объявленные переменные. Исправьте
# эту ошибку и убедитесь, что nums_list, some_dict и uniq_nums не меняются.
import random


def change_dict(dct):
    num = random.randint(1, 100)
    for i_key, i_value in dct.items():
        if isinstance(i_value, list):
            i_value = i_value + [num]
            common_dict[i_key] = i_value
        if isinstance(i_value, dict):
            i_value[num] = i_key

            # common_dict[i_key[num]] = i_key
            # print(common_dict[i_key])
            # common_dict[i_key].update({num: i_key})
            # return num
            # some_dict.pop(num)
            # common_dict[i_key] = i_value.popitem()
            # print(i_value)
        if isinstance(i_value, set):
            i_value.add(num)
            # new_uniq_nums = i_value
            # new_uniq_nums.add(num)
            # print(new_uniq_nums)
    # print(common_dict)

nums_list = [1, 2, 3]
some_dict = {1: 'text', 2: 'another text'}
uniq_nums = {1, 2, 3}

common_dict = {1: nums_list, 2: some_dict, 3: uniq_nums, 4: (10, 20, 30)}
# print(common_dict)
# number = change_dict(common_dict)
change_dict(common_dict)
print(common_dict)
print(nums_list)
# some_dict.pop(number)  # ?????
print(some_dict)
print(uniq_nums)
