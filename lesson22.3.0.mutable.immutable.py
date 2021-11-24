x = 10
y = x
print('x, id(x):', x, id(x))
print('y, id(y):', y, id(y))
print('id(x) == id(y):', id(x) == id(y))

x += 1
print('x, id(x):', x, id(x))
print('y, id(y):', y, id(y))

list_1 = [1, 2, 3]
list_2 = list_1
print('list_1, id(list_1):', list_1, id(list_1))
print('list_2, id(list_2):', list_2, id(list_2))
list_2.append(100)
list_2 += [100]
print('list_1, id(list_1):', list_1, id(list_1))
print('list_2, id(list_2):', list_2, id(list_2))