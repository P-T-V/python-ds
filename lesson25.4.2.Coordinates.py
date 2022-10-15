class Point:
    index = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Point.index += 1
        self.print_info()

    def print_info(self):
        print(f'Point number {Point.index}: x = {self.x}, y = {self.y}')


point1 = Point()
# point1.print_info()
point2 = Point(10, 20)
# point2.print_info()
