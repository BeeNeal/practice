# problem to solve:
# The user expecation yields multiple, related objects

from factory import *

class DogFactory(object):
    """ Concrete Factory"""

    def get_pet(self):
        """Return a dog object"""

        return Dog()

    def get_food(self):
        """Return a dog food object"""

        return "dog food"

class PetStore(object):
    """ PetStore houses our abstract factory"""

    def __init__(self, pet_factory=None):
        """ pet_factory is our Abstract factory"""

    def show_pet(self):
        """Utility method to display details of objects from by the Dogfactory"""

        print("Our pet is '{}'!".format(pet))
        print("Our pet says hello by '{}'".format(pet.speak()))
        print("Its food is '{}'!".format(pet_food))
