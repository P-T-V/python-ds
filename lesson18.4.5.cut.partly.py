import random

n = int(input('Number: '))

n_list = [random.randint(-100, 101) for x in range(n)]
a = random.randint(0, n-1)
b = random.randint(0, n-1)
if a > b:
    a, b = b, a
print(n_list)
print(a)
print(b)

# new_list = [n_list[i] for i in range(n) if (i < a or i > b)]
# print(new_list)
n_list = [n_list[i] for i in range(n) if (i < a or i > b)]
print(n_list)
