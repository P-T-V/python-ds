incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

for i_key, i_item in incomes.items():
    print('{key}--{item}'.format(
        key=i_key,
        item=i_item
    ))
    