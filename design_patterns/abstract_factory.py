# problem to solve:
# The user expecation yields multiple, related objects

class Dog(object):
    """One of the dog objects to be returned"""

    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"


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

        self._pet_factory = pet_factory
        # all we need to store instance of concrete factory class

    def show_pet(self):
        """Utility method to display details of objects from by the Dogfactory"""

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is '{}'!".format(pet))
        print("Our pet says hello by '{}'".format(pet.speak()))
        print("Its food is '{}'!".format(pet_food))

factory = DogFactory()
shop = PetStore(factory)

shop.show_pet()
