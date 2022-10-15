import random


class Toyota:
    color = 'red'
    price = 2000000
    max_speed = 250
    current_speed = 0


model_1 = Toyota()
model_2 = Toyota()
model_3 = Toyota()
list_models = [model_1, model_2, model_3]
for i in range(3):
    list_models[i].current_speed = random.randint(0, 201)
    print(f'Speed {list_models[i]} =', list_models[i].current_speed)
    print(f'Speed model_{i+1} =', list_models[i].current_speed)
