user_name = input('Введите имя: ')
user_debt = int(input('Введите долг: '))

text = '{0}! {0}, привет! Как дела, {0}? Где мои {1} рублей? {0}! {1} рублей!!'.format(
    user_name,
    user_debt
)
print(text)
