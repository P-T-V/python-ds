def factorial(num):
    if num == 1:
        return 1
    fact_n_minus_1 = factorial(num - 1)
    return num * fact_n_minus_1


number = int(input('Введите число для расчёта факториала: '))
num_fact = factorial(number)
print('Факториал числа: {numb}! = {numb_f}'.format(
    numb=number,
    numb_f=num_fact
))
