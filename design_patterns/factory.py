class Dog(object):
    """ Dog class"""

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "woof!"


class Cat(object):
    """ Cat class"""

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "meow!"


def get_pet(pet="dog"):
    """The factory method."""

    pets = dict(dog=Dog("Barxter"), cat=Cat('Meowza'))

    return pets[pet]

d = get_pet('dog')
c = get_pet('cat')

# Encapulates object creation
# Useful when have uncertainties in types of objects

if __name__ == "__main__":

    print d.speak()
    print c.speak()
