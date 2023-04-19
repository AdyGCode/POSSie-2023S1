from animal import Animal

if __name__ == "__main__":
    cat = Animal(colour="red")
    cat.set_name("Custard")
    cat.set_species("cat")
    cat.set_colour("Orange")
    print(cat.get_name())
    print(cat.get_species())
    print(cat.get_colour())

    dog = Animal(species="dog", name="Buster", colour="Red")
    print(dog.get_name())
    print(dog.get_species())
    print(dog.get_colour())
