# some_object = 'О Дивный Новый мир!'
# some_object = [100, 200, 300, 'буква', 0, 2, 'а']
some_object = {100: 200, 300: 'буква', 2: 'а', 0: 1}
# some_object = (100, 200, 300, 'буква', 0, 2, 'а')
some_object_list = list()

if isinstance(some_object, (str, list, tuple)):
    for i_index, i_symbol in enumerate(some_object):
        if i_index % 2 == 0:
            some_object_list.append(i_symbol)

if isinstance(some_object, dict):
    for i_index, i_symbol in enumerate(some_object):
        # print(i_index, i_symbol)
        if i_index % 2 == 0:
            some_object_list.append(some_object.get(i_symbol))

print(some_object_list)
