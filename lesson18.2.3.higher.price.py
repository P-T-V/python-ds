def higher_price(price, percent):
    return round(price * (1 + percent / 100), 2)


price_list = [float(input('Цена на товар: ')) for a in range(5)]
frst_prct = int(input('Повышение на первый год: '))
snd_prct = int(input('Повышение на второй год: '))
prices_frst = [higher_price(i_price, frst_prct) for i_price in price_list]
prices_snd = [higher_price(i_price, snd_prct) for i_price in prices_frst]

print('Сумма цен за каждый год:', round(sum(price_list), 2), round(sum(prices_frst), 2), round(sum(prices_snd), 2))
