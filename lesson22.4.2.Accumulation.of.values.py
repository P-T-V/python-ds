def add_num(num, lisst=None):
    if lisst is None:
        lisst = list()
    lisst.append(num)
    new_list.extend(lisst)
    print('Num', num, 'added. Current list:', lisst)
    print('Num', num, 'added. Current new_list:', new_list)


new_list = list()
add_num(5)
add_num(10)
add_num(15)


def accumulation(number, lst=list()):
    lst.append(number)
    print('Num', number, 'added. Current list:', lst)


print()
accumulation(5)
accumulation(10)
accumulation(15)
