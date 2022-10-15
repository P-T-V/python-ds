class Toyota:

    def __init__(self, color, price, max_speed, current_speed):
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.current_speed = current_speed

    def print_info(self):
        print(
            'Color: {}\nPrice: {}\nMax speed: {}\nCurrent speed: {}\n'.format(
                self.color, self.price, self.max_speed, self.current_speed
            )
        )

    def cur_speed(self, speed):
        self.current_speed = speed


model_1 = Toyota('red', 2000000, 250, 0)
model_1.print_info()
new_speed = int(input('Pls, input current speed: '))
model_1.cur_speed(new_speed)
print('New data:')
model_1.print_info()
