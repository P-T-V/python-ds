def add_num(seq, number):
    seq = list(seq)
    for i_num in range(len(seq)):
        seq[i_num] += number
    return seq


origin_tuple = (3, 1, 4, 1, 5)
changed_list = add_num(origin_tuple, 5)
print(origin_tuple)
print(changed_list)


nums = (10, 20, 30, 40)
print('\nnums =', nums)
print('nums[1] =', nums[1])
print('nums.index(30) =', nums.index(30))
print('nums[1:] =', nums[1:])
print('5 in nums =', 5 in nums)

some_list = [1, 1, 1]
new_nums = (10, 20, 30, some_list)
print('\nsome_list =', some_list)
print('new_nums = ', new_nums)
new_nums[3][0] = 100
print('new_nums[3][0] = 100 =>', new_nums)  # Some_list это ссылка на список внутри кортежа. А ссылку не изменяли

user = 'Vova', 'Petrov', 25
print('\nuser = "Vova", "Petrov", "25" =>', user)
name, surname, age = user
print('name, surname, age = user =>')
print('name =', name)
print('surname =', surname)
print('age =', age)

def get_user():
    user1 = 'Bob'
    surname1 = 'Petrov'
    age1 = 20
    return user1, surname1, age1
user1 = get_user()
print('\nuser1 =>', user1)
