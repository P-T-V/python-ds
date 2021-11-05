small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}

big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}

big_storage.update(small_storage)
item = input('Введите название товара: ')
print(big_storage.get(item))
if item in big_storage:
    big_storage['new name'] = big_storage.pop(item)
print(big_storage)
