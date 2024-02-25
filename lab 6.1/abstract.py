from abc import ABC, abstractmethod

"""Lab 6.1 - Abstract Classes

Vincenzo Meschi and Anis Huric
"""

class Pet(ABC):
    def __init__(self, name, age, species):
        self.__name = name
        self.__age = age
        self.__species = species

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def species(self):
        return self.__species

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def sleep(self):
        pass
    
    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.species}"
    
    
class Dog(Pet):
    def __init__(self, name, age, species, breed):
        super().__init__(name, age, species)
        self.__breed = breed

    @property
    def breed(self):
        return self.__breed

    def speak(self):
        return "Woof"

    def eat(self):
        return "Eating kibble"

    def play(self):
        return "Playing fetch"

    def sleep(self):
        return "Sleeping on the couch"
    
    def __str__(self):
        return f"{super().__str__()} and is a {self.breed}"
    

class Cat(Pet):
    def __init__(self, name, age, species, color):
        super().__init__(name, age, species)
        self.__color = color

    @property
    def color(self):
        return self.__color

    def speak(self):
        return "Meow"

    def eat(self):
        return "Eating wet food"

    def play(self):
        return "Playing with a toy"

    def sleep(self):
        return "Sleeping on the bed"
    
    def __str__(self):
        return f"{super().__str__()} and is {self.color}"
    

class Bird(Pet):
    def __init__(self, name, age, species, wingspan):
        super().__init__(name, age, species)
        self.__wingspan = wingspan

    @property
    def wingspan(self):
        return self.__wingspan

    def speak(self):
        return "Chirp"

    def eat(self):
        return "Eating seeds"

    def play(self):
        return "Playing with a bell"

    def sleep(self):
        return "Sleeping in a nest"
    
    def __str__(self):
        return f"{super().__str__()} and has a wingspan of {self.wingspan} inches"
    

if __name__ == "__main__":
    dog = Dog("Rex", 5, "Dog", "Golden Retriever")
    cat = Cat("Whiskers", 3, "Cat", "Grey")
    bird = Bird("Polly", 2, "Bird", 10)
    
    print(dog)
    print(cat)
    print(bird)
    
    print(dog.speak())
    print(cat.eat())
    print(bird.play())
    print(dog.sleep())
