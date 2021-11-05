incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}
# print(incomes)
print('\nОбщий доход за год составил:', sum(incomes.values()))

for item in incomes:
    if incomes[item] == min(incomes.values()):
        print('Самый маленький доход у', item, '. Он составляет', incomes[item])
        bad_fruit = item

incomes.pop(bad_fruit)
print('Итоговый словарь:', incomes)
