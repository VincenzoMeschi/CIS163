from abc import ABC, abstractmethod
from typing import List


class Question(ABC):
    def __init__(self, title: str, desc: str, points: int) -> None:
        self.__title = title
        self.__description = desc
        self.__points = points

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        self.__title = title

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, desc):
        if not isinstance(desc, str):
            raise TypeError("Description must be a string")
        self.__description = desc

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, points):
        if not isinstance(points, (int, float)):
            raise TypeError("Points must be an integer or float")
        if points < 0:
            raise ValueError("Points must be a positive number")
        self.__points = points

    @abstractmethod
    def attempt(self, *args) -> bool:
        pass

    def __str__(self) -> str:
        return f"{self.title}: {self.description}"


class MultipleChoice(Question):
    def __init__(
        self,
        title: str,
        desc: str,
        answers: List[str],
        correct_answer: str,
        points: int,
    ) -> None:
        super().__init__(title, desc, points)
        if correct_answer not in answers:
            raise ValueError("Correct answer must be in answers")
        self.__answers = answers
        self.__correct_answer = correct_answer

    def attempt(self, answer: str) -> bool:
        if answer in self.__answers:
            return answer == self.__correct_answer
        return False

    def __str__(self) -> str:
        return f"{super().__str__()}\n\t1. {self.__answers[0]}\n\t2. {self.__answers[1]}\n\t3. {self.__answers[2]}\n\t4. {self.__answers[3]}"


class Essay(Question):
    def __init__(
        self, title: str, desc: str, points: int, correct_answers: str
    ) -> None:
        super().__init__(title, desc, points)
        if not isinstance(correct_answers, str):
            raise TypeError("Correct answers must be a string")
        self.__correct_answers = correct_answers

    def attempt(self, answer: str, auto_grade: bool = False) -> bool:
        if auto_grade:
            if answer in self.__correct_answers:
                return True
            return False
        return "This will be manually graded"


class ShortAnswer(Essay):
    # if answer has over 250 characters, it will return false
    def attempt(self, answer: str, auto_grade: bool = False) -> bool:
        if len(answer) > 250:
            return False
        return super().attempt(answer, auto_grade)
