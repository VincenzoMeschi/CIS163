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
        self.__state = {"val": self.seed, "ndigits": len(str(self.seed))}

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
        self.__state = {"val": seed, "a": a, "c": c, "m": m}

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


class LaggedFibonacci:
    def __init__(self, seed, j: int, k: int, m: int) -> None:
        self.__state = dict()
        if isinstance(seed, list) and all(isinstance(item, int) for item in seed):
            self.__state["val"] = seed
            self.seed = seed.copy()
        else:
            raise TypeError("Seed must be list of int")

        if isinstance(m, int):
            self.__state["m"] = m
        else:
            raise ValueError("Param M must be an integer")

        if len(str(k)) < len(seed):
            self.__state["k"] = k
            if j > 0 and j < k:
                self.__state["j"] = j
            else:
                raise ValueError("Param J must be greater than 0 and less than k")
        else:
            raise ValueError("Param k's length must be less than the length of seed")

    def __iter__(self):
        return self

    def __next__(self):
        first_digit = self.__state["val"][-(self.__state["k"])]
        second_digit = self.__state["val"][-(self.__state["j"])]
        number = (first_digit + second_digit) % self.__state["m"]

        self.__state["val"][:-1] = self.__state["val"][1:]
        self.__state["val"][-1] = number

        if self.__state["val"] == self.seed:
            raise StopIteration()

        return number

    def get_state(self) -> dict:
        return self.__state.copy()

    def set_state(self, state: dict) -> None:
        if "val" in state and "j" in state and "k" in state and "m" in state:
            self.__state = state
            self.seed = state["val"]
        else:
            raise ValueError("Invalid dictionary. Must include keys val, j, k, m")


class Acorn:
    def __init__(self, seed: list[int], M: int) -> None:
        self.__state = dict()

        if isinstance(seed, list) and all(isinstance(item, int) for item in seed):
            self.__state["vals"] = seed
        else:
            raise TypeError("Seed must be list of int")

        if isinstance(M, int):
            self.__state["M"] = M
        else:
            raise ValueError("Param M must be an integer")

        self.start = seed.copy()

    def __iter__(self):
        return self

    def __next__(self):
        state = self.__state
        new_vals = state["vals"].copy()

        for i in range(1, len(state["vals"])):
            new_vals[i] = (new_vals[i - 1] + new_vals[i]) % state["M"]

        if new_vals == self.start:
            raise StopIteration()

        state["vals"] = new_vals

        return new_vals

    def get_state(self) -> dict:
        return self.__state.copy()

    def set_state(self, state: dict) -> None:
        if "vals" in state and "M" in state:
            self.__state = state
            self.start = state["vals"]
        else:
            raise ValueError("Invalid dictionary. Must include keys vals, M")


class Analyzer:
    def __init__(self, rand_num_gen: object) -> None:
        self.rand_num_gen = rand_num_gen
        self.max = float("-inf")
        self.min = float("inf")
        self.average = 0.0
        self.period = 0
        self.bit_freqs = []

    def analyze(self, max_nums=1e10):
        nums = []
        total, count, acorn_period_count = 0, 0, 0
        is_acorn = False

        for num in self.rand_num_gen:
            if isinstance(num, int):
                if count >= max_nums:
                    break

                nums.append(num)
                total += num
                count += 1
            elif isinstance(num, list):
                is_acorn = True
                acorn_period_count += 1
                for i, j in enumerate(num):
                    if i != 0:
                        nums.append(j)
                        total += j
                        count += 1
            else:
                raise TypeError("Random number generator must return int or list[int]")

        self.max = max(nums)
        self.min = min(nums)
        self.average = total / count if count > 0 else 0
        print(f"{self.average} == {total} / {count}")
        if is_acorn:
            self.period = min(max_nums, acorn_period_count)
        else:
            self.period = min(max_nums, count)

        bit_length = len(bin(self.max)) - 2

        self.bit_freqs = [0 for _ in range(bit_length)]

        # bit_freqs
        for num in nums:
            if isinstance(num, int):
                temp = bin(num)[2:].zfill(bit_length)
                for i, j in enumerate(temp):
                    if j == "1":
                        self.bit_freqs[i] += 1
            elif isinstance(num, list):
                for i in range(1, len(num)):
                    temp = bin(num[i])[2:].zfill(bit_length)
                    for i, j in enumerate(temp):
                        if j == "1":
                            self.bit_freqs[i] += 1


a = Acorn([7, 6, 8, 11, 5], 23)


analyzer = Analyzer(a)

analyzer.analyze()

print(analyzer.max)
print(analyzer.min)
print(analyzer.average)
print(analyzer.period)
print(analyzer.bit_freqs)

print("============================")
