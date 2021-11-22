import math


def cylinder(rad, hei):
    side_cyl = round(2 * math.pi * rad * hei, 2)
    full_cyl = round(side_cyl + 2 * math.pi * rad**2, 2)
    return side_cyl, full_cyl


r = int(input('введите радиус: '))
h = int(input('введите высоту: '))
side, full = cylinder(r, h)
print('Площадь боковой поверхности цилиндра:', side)
print('Полная площадь цилиндра:', full)
