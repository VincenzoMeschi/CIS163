"""Random Number Generation Project (1)

This module will have many different methods of handling
random number generation. We will use the Middle Square Method,
Linear Congruential Generators, Lagged Fibonacci Generators,
and the Acorn Method. 

Extra Information:

  Author: Vincenzo Meschi
  Date: 2024-01-22
  Version: Python 3.10.12 (python3 --version)
"""

# print(int(str(5655).zfill(10)))


class MiddleSquare:
    def __init__(self, seed: int) -> None:
        if isinstance(seed, int):
            if len(str(seed)) % 2 == 0:
                self.seed = seed
            else:
                raise ValueError("Seed must have an even amount of digits")
        else:
            raise TypeError('Parameter "seed" must be of type int')
        self.seen = set()
        self.__state = {"val": seed, "ndigits": len(str(seed))}

    def __iter__(self):
        return self

    def __next__(self):
        state = self.__state

        state["val"] = state["val"] ** 2

        str_val = str(state["val"])
        str_val = str_val.zfill(2 * state["ndigits"])
        state["val"] = int(
            str_val[(state["ndigits"] // 2) : (3 * state["ndigits"] // 2)]
        )

        if state["val"] in self.seen:
            raise StopIteration()

        self.seen.add(state["val"])
        return state["val"]

    def get_state(self) -> dict:
        return self.__state.copy()

    def set_state(self, state: dict) -> None:
        if "val" in state and "ndigits" in state:
            self.__state = state
        else:
            raise ValueError("Invalid dictionary. Must include keys val and ndigits")


class LinearCongruential:
    def __init__(self, seed: int, a: int, c: int, m: int) -> None:
        if isinstance(seed, int):
            self.seed = seed
        else:
            raise TypeError('Parameter "seed" must be of type int')
        self.seen = set()
        self.__a = a
        self.__c = c
        self.__m = m
        self.__state = {"val": seed, "a": self.__a, "c": self.__c, "m": self.__m}

    def __iter__(self):
        return self

    def __next__(self):
        state = self.__state

        state["val"] = (state["a"] * state["val"] + state["c"]) % state["m"]

        if state["val"] in self.seen:
            raise StopIteration()

        self.seen.add(state["val"])
        return state["val"]

    def get_state(self) -> dict:
        return self.__state.copy()

    def set_state(self, state: dict) -> None:
        if "val" in state and "a" in state and "c" in state and "m" in state:
            self.__state = state
            self.seen.clear()
        else:
            raise ValueError("Invalid dictionary. Must include keys val, a, c, m")
