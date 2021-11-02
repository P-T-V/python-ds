user_name = input('Имя: ')
order_numb = int(input('Номер заказа: '))

# text = 'Здравствуйте, {user}! Ваш номер заказа: {order}. Приятного дня!'.format(
#     user=user_name,
#     order=order_numb
# )
text = 'Здравствуйте, {0}! Ваш номер заказа: {1}. Приятного дня!'.format(
    user_name,
    order_numb
)

print(text)
