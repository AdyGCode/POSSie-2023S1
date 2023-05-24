class Vehicle:


    def __init__(self, wheels=None, colour=None):
        # Constructor for the vehicle class
        self.wheels = wheels
        self.colour = colour

    def start(self):
        pass

    def set_wheels(self, number=4):
        self.wheels = number


class Car(Vehicle):
    # inherits wheels, colour, start
    def __init__(self, wheels=None, colour=None):
        # call the parent constructor
        super().__init__(wheels, colour)


bmw = Car(4, None)
