import turtle


class Drawer:
    """ Responsible for defining an interface for drawing """

    def __init__(self):
        pass

    def select_pen(self, pen_num):
        print(f'Selected pen {pen_num}')

    def pen_down(self):
        print('pen down')

    def pen_up(self):
        print('pen up')

    def draw_line(self, direction, distance):
        print(f'drawing line of length {distance} at {direction}')


class TurtleDrawer(Drawer):

    def __init__(self):
        super().__init__()
        self.my_drawer = turtle.Turtle("turtle")
        self.my_drawer.getscreen().mode(mode='logo')
        self.is_pen_down = True
        self.my_drawer.screen.setup(1000, 700)
        self.my_drawer.color('blue')
        self.message = ''

    def select_pen(self, pen_num):
        self.my_drawer.pensize(pen_num)
        if pen_num > 100:
            # print('Limit the pen size from 1 to 100. Set the pensize again')
            self.message = 'Limit the pen size from 1 to 100. Set the pensize again'
            print(f'{self.message}')
        else:
            # print(f'Pen size is set to {pen_num}')
            self.message = f'Pen size is set to {pen_num}'
            print(f'{self.message}')

    def pen_down(self):
        self.my_drawer.pendown()
        self.is_pen_down = True
        # print("Pen is down! You may start drawing")
        self.message = 'Pen is down! You may start drawing'
        print(f'{self.message}')

    def pen_up(self):
        self.my_drawer.penup()
        self.is_pen_down = False
        # print("Pen is up! Unable to draw")
        self.message = 'Pen is up! Unable to draw'
        print(f'{self.message}')

    def draw_line(self, direction, distance):
        #  13. Error trapping & handling
        if self.is_pen_down:
            self.my_drawer.setheading(direction)
            self.my_drawer.forward(distance)
            self.message = f'drawing line of length {distance} at {direction} direction'
            print(self.message)
        else:
            # print(f"Unable to draw because the Pen is up\n ")
            self.message = f'Unable to draw because the Pen is up\n'
            print(f'{self.message}')
