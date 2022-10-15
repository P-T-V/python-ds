class Toyota:
    color = 'red'
    price = 2000000
    max_speed = 250
    current_speed = 0

    def info(self):
        print(
            'Color: {}\nPrice: {}\nMax speed: {}\nCurrent speed: {}\n'.format(
                self.color, self.price, self.max_speed, self.current_speed
            )
        )

    def cur_speed(self, speed):
        self.current_speed = speed

model_1 = Toyota()
model_2 = Toyota()
model_3 = Toyota()
list_models = [model_1, model_2, model_3]
for i in range(3):
    new_speed = int(input('Pls, input current speed: '))
    list_models[i].cur_speed(new_speed)
    print('New data:')
    list_models[i].info()
