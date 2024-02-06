import datetime


class Item:
    def __init__(self, id: int, name: str):
        self._id = id
        self._name = name
        self._due_date = datetime.date.today()
        self._checked_out = False

    def __str__(self) -> str:
        return str(self._id) + ": " + self._name

    def check_out(self):
        print("You can't check out this item")

    def __add_days__(self, days_):
        self._due_date = self._due_date + datetime.timedelta(days=days_)
        print(str(self) + " is due back on " + str(self._due_date))


class Book(Item):
    def __init__(self, id: int, name: str, dewey: str):
        super().__init__(id, name)
        self._dewey = dewey

    def __str__(self) -> str:
        s = super().__str__()
        s = s + " located at " + self._dewey
        return s

    def check_out(self):
        self._checked_out = True
        self.__add_days__(14)


class Video(Item):
    def __init__(self, id: int, name: str, type: str):
        super().__init__(id, name)
        self._type = type

    def __str__(self) -> str:
        s = super().__str__()
        s = s + " is of type " + self._type
        return s

    def check_out(self):
        self._checked_out = True
        self.__add_days__(7)


class Game(Item):
    def __init__(self, id: int, name: str, platform: str):
        super().__init__(id, name)
        self._platform = platform

    def check_out(self):
        self._checked_out = True
        self.__add_days__(2)
