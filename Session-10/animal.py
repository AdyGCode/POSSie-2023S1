class Animal:

    # Constructor
    def __init__(self, species=None, name=None, colour=None):
        self.name = name
        self.species = species
        # self.colour = colour
        self.set_colour(colour)

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_species(self, name):
        self.species = name

    def get_species(self):
        return self.species

    def set_colour(self, colour):
        if colour is None:
            raise ValueError("Colour Required")
        if type(colour) is not str:
            raise TypeError("Colour must be a string")
        self.colour = colour

    def get_colour(self):
        return self.colour

