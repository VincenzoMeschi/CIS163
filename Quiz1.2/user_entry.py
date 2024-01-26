from typing import List


class Movie:
    def __init__(
        self, title: str, genre: List[str], director: str, year: int, cast: List[str]
    ):
        self.__title = title
        self.__genre = genre
        self.__director = director
        self.__year = year
        self.__cast = cast

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        if isinstance(title, str):
            self.__title = title

    @property
    def website(self) -> str:
        temp = self.__title
        temp = temp.lower().replace(" ", "")
        return f"www.{temp}.com/"
