a = int(input('Insert start number A: '))
b = int(input('Insert end number B: '))

squares = [x ** 2 for x in range(a, b + 1)]
qubes = [x ** 3 for x in range(a, b + 1)]
print('Cubes of numbers ranging from A to B:', qubes)
print('Squares of numbers ranging from A to B:', squares)
