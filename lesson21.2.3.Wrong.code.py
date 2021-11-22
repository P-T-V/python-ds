import random


def change(nums):
    nums_list = list(nums)
    index = random.randint(0, 4)
    value = random.randint(100, 1000)
    nums_list[index] = value
    return tuple(nums_list), value


my_nums = 1, 2, 3, 4, 5
print('my_nums:', my_nums)
new_nums, rand_val = change(my_nums)
print(new_nums, ',', rand_val)
new_nums2, rand_val2 = change(new_nums)
rand_val += rand_val2
print(new_nums2, ',', rand_val)
