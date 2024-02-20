from abc import ABC, abstractmethod
from random import randint

# Game - Abstract
# ===================
# - what attributes does the abstract need?
# - what methods?
#
#
# Choose two to three of the below. And then create concrete classes of them
#  - make sure they habve any addtional attributes
#  - make at least one unique method


class Game(ABC):
    def __init__(self, players) -> None:
        self.players = players

    @abstractmethod
    def end(self):
        pass


#  hearts = 0, clubs = 1, spades = 2, diamonds = 3
#  hearts = 0, clubs = 1, spades = 2, diamonds = 3
class Cards(Game):
    def __init__(self):
        super().__init__()
        self.cards = [[0] * 13, [0] * 13, [0] * 13, [0] * 13]

    def shuffle(self):
        self.cards = [[0] * 13, [0] * 13, [0] * 13, [0] * 13]

    @abstractmethod
    def draw(self) -> str:
        suit = randint(0, 3)
        card = randint(0, 13)

        chosen_card = self.cards[suit][card]
