goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
print('\nТекущий ассортимент:', goods)

fruit_name = input('\nНовый фрукт: ')
price = int(input('Цена: '))

goods.append([fruit_name, price])

print('\nНовый ассортимент:', goods)

for i_goods in range(len(goods)):
    goods[i_goods][1] = round(goods[i_goods][1] * 1.08, 2)

print('\nНовый ассортимент с увел. ценой:', goods)
