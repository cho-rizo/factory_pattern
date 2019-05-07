from abc import ABC, abstractmethod


# Creator classes
from product_classes import Dog, Cat


class PetShop(ABC):
    @abstractmethod
    def make_animal(self, animal_type):
        pass

    def buy_animal(self, animal_type):
        animal = self.make_animal(animal_type)
        animal.makes_sound_to_prove_its_alive()


class DogShop(PetShop):
    @staticmethod
    def make_animal(animal_type):
        return Dog()


class CatShop(PetShop):
    @staticmethod
    def make_animal(animal_type):
        return Cat()

dog_shop = DogShop()
dog_shop.buy_animal("Dog")

