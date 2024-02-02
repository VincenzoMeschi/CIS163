class Media:
    def __init__(self, name: str, year: int):
        self.__name = name
        self.__year = year

    @property
    def name(self):
        return self.__name

    @property
    def year(self):
        return self.__year

    def __str__(self):
        return self.__class__.__name__


class Game(Media):
    def __init__(self, name: str, year: int, manufacturer: str, players: int = 1):
        super().__init__(name=name, year=year)
        self.__manufacturer = manufacturer
        self.__players = players

    @property
    def players(self) -> str:
        return self.__players

    @players.setter
    def players(self, num: int) -> None:
        if isinstance(num, int):
            if num < 1:
                self.__players = 1
            else:
                self.__players = num
        else:
            self.__players = -1

    def __str__(self):
        sr = super().__str__()
        return f"{sr}\nName: {self.__name}\nYear: {self.__year}\nNo. Players: {self.players}"
