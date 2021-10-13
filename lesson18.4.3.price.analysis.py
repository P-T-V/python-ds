import random

original_prices = [random.randint(-10, 50) for _ in range(7)]

# new_prices = original_prices[:]

new_prices = [(i_price if i_price > 0 else 0) for i_price in original_prices]

# for i in range(len(original_prices)):
#
#     if new_prices[i] < 0:
#
#         new_prices[i] = 0
print(original_prices)
print(new_prices)
print("Мы потеряли:",  sum(original_prices) - sum(new_prices))
