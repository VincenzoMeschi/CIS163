from abc import ABC, abstractmethod


class Cup(ABC):
    
    @abstractmethod
    def drink_all(self):
        pass


    @abstractmethod
    def fill(self, amount):
        pass

    @abstractmethod
    def get_contents(self):
        pass

class Coffee(Cup):
    def __init__(self, contents) -> None:
        self.contents = contents
        self.amount_in_oz = 16

    def get_contents(self):
        return self.contents
    
    def drink_all(self):
        self.amount_in_oz = 0

    def fill(self, amount):
        self.amount_in_oz = amount
        if amount > 16:
            print(f"Cup has overflown! Now contains {amount} ounces of {self.contents}")



