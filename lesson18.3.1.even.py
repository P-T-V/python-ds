a = int(input('Insert start number A: '))
b = int(input('Insert end number B: '))

even_list = [x for x in range(a, b + 1) if x % 2 == 0]
print(even_list)
