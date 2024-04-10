from __future__ import annotations
from typing import Optional

class TrainCar:

    def __init__(self, weight: int, next: Optional[TrainCar] = None):
        self.weight = weight
        self.next = next

    def __str__(self):
        return f"|{self.weight}|"


class Train:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__length = 0
        self.__pointer = None
    
    @property
    def head(self) -> Optional[TrainCar]:
        return self.__head
    
    @property
    def length(self) -> int:
        return self.__length
    
    def push(self, weight: int) -> None:
        new_car = TrainCar(weight)
        if self.__head is None:
            self.__head = new_car
            self.__tail = new_car
        else:
            self.__tail.next = new_car
            self.__tail = new_car
        self.__length += 1
    
    def pop(self) -> int:
        if self.__head is None:
            raise IndexError
        weight = self.__head.weight
        self.__head = self.__head.next
        self.__length -= 1
        return weight
    
    def __iter__(self):
        self.__pointer = self.__head
        return self
    
    def __next__(self) -> TrainCar:
        if self.__pointer is None:
            raise StopIteration
        car = self.__pointer
        self.__pointer = self.__pointer.next
        return car
    
    def __str__(self) -> str:
        if self.__head is None:
            return "Train: None"
        result = "Train"
        for car in self:
            result += f" {car}"
        return result

def process_train(p1: int, p2: int, p3: int, car: Optional[TrainCar]=None) -> bool:
    if car is None:
        return True
    if p1 >= car.weight and process_train(p1 - car.weight, p2, p3, car.next):
        return True
    if p2 >= car.weight and process_train(p1, p2 - car.weight, p3, car.next):
        return True
    if p3 >= car.weight and process_train(p1, p2, p3 - car.weight, car.next):
        return True
    return False

