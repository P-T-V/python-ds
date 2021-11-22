import random


tuple1 = tuple([random.randint(0, 5) for _ in range(6)])
tuple2 = tuple([random.randint(-5, 0) for _ in range(6)])
print('кортеж десятью случайными целыми числами от 0 до 5 включительно:', tuple1)
print('кортеж числами от −5 до 0:', tuple2)
tuple3 = tuple1 + tuple2
print('Объединение двух кортежей - третий кортеж:', tuple3)
num = tuple3.count(0)
print('количество нулей в нём:', num)
