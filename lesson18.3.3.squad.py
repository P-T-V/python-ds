import random

squad_1 = [random.randint(50, 80) for _ in range(10)]
squad_2 = [random.randint(30, 60) for _ in range(10)]
squad_3 = [('Погиб' if squad_1[i_dmg] + squad_2[i_dmg] > 100
            else 'Выжил') for i_dmg in range(10)]

print('Урон первого отряда:', squad_1)
print('Урон второго отряда:', squad_2)
print('Состояние третьего отряда:', squad_3)
