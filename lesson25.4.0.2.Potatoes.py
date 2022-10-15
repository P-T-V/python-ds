class Potato:
    states = {0: 'None', 1: 'Sprout', 2: 'Immature', 3: 'Mature'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print(f'Potato {self.index} now is {Potato.states[self.state]}')


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Potato is growing')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('The potatoes are not ripe yet\n')
        else:
            print('All potatoes are ripe. You can collect!\n')


my_garden = PotatoGarden(5)
my_garden.are_all_ripe()
for _ in range(3):
    my_garden.grow_all()
    my_garden.are_all_ripe()
    