def print_tax_document(tax, *args, **kwargs):
    price_sum = 0
    for i_price in args:
        price_sum += i_price * (1 - tax / 100)
    print('Сумма цен с учётом налога:', price_sum)
    for i_info, i_value in kwargs.items():
        print('{}: {}'.format(i_info, i_value))


my_tax = int(input('Величина налога: '))
print_tax_document(my_tax, 1000, 950, 880, 980, 970,
                   year=1997,
                   doc_type='Report',
                   operation_id=1598754685)


def print_storage(name, good_1=None, good_2=None, good_3=None):
    print('\nStorage name:', name)
    print(good_1, "is stored in section 1")
    print(good_2, "is stored in section 2")
    print(good_3, "is stored in section 3")


print_storage('Shop', 'Box')
