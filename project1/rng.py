"""Random Number Generation Project (1)

This module will have many different methods of handling
random number generation. We will use the Middle Square Method,
Linear Congruential Generators, Lagged Fibonacci Generators,
and the Acorn Method.

Also includes an Analyzer class to analyze the generated numbers.

Extra Information:

  Author: Vincenzo Meschi
  Date: 2024-01-22
  Version: Python 3.10.12 (python3 --version)
"""


class MiddleSquare:
    """Middle Square Random Number Generator.

    This class implements a random number generator using the Middle Square method.
    It generates a sequence of random numbers based on a seed value.

    Attributes:
        seed (int): The seed for the random number generator.
        seen (set): A set to keep track of the generated numbers.
        __state (dict): The internal state of the generator.

    Raises:
        ValueError: If the seed does not have an even amount of digits.
        TypeError: If the seed is not of type int.
        StopIteration: If the number has been seen before.
    """

    def __init__(self, seed: int) -> None:
        """Initializes the MiddleSquare class.

        Args:
            seed (int): The seed for the random number generator.

        Raises:
            ValueError: Seed must have an even amount of digits.
            TypeError: Parameter "seed" must be of type int.
        """
        # Validate the seed's type
        if isinstance(seed, int):
            # Check if the seed has an even amount of digits
            if len(str(seed)) % 2 == 0:
                self.seed = seed
            else:
                raise ValueError("Seed must have an even amount of digits")
        else:
            raise TypeError('Parameter "seed" must be of type int')

        # Initialize the set to keep track of the generated numbers. Sets are used to avoid duplicates.
        self.seen = set()

        # Initialize the internal state of the generator.
        self.__state = {"val": self.seed, "ndigits": len(str(self.seed))}

    # Implement the iterator protocol
    def __iter__(self):
        # Only return self, as the __next__ method is implemented in the class.
        return self

    def __next__(self):
        """Generates the next random number.

        Raises:
            StopIteration: If the number has been seen before.

        Returns:
            int: The next random number.
        """

        # Assign the state to a local variable
        state = self.__state

        # Square the value and convert it to a string
        state["val"] = state["val"] ** 2
        str_val = str(state["val"])

        # Zero-pad the string if necessary so that it has 2*n digits
        str_val = str_val.zfill(2 * state["ndigits"])

        # Use the middle n digits as the next value by imagining the string as fourths and taking from 2/4 to 3/4
        state["val"] = int(
            str_val[(state["ndigits"] // 2) : (3 * state["ndigits"] // 2)]
        )

        # If the number has been seen before, raise a StopIteration
        if state["val"] in self.seen:
            raise StopIteration()

        # Add the number to the set of seen numbers
        self.seen.add(state["val"])
        return state["val"]

    def get_state(self) -> dict:
        # Return a copy of the internal state so it cannot be mutated
        return self.__state.copy()

    def set_state(self, state: dict) -> None:
        # Verify that the dictionary is valid and set the internal state
        if "val" in state and "ndigits" in state:
            self.__state = state
        else:
            raise ValueError("Invalid dictionary. Must include keys val and ndigits")


class LinearCongruential:
    """Linear Congruential Generator for generating random numbers.

    The LinearCongruential class represents a random number generator based on the linear congruential method.
    It generates a sequence of random numbers using a linear equation.

    Attributes:
        seed (int): The seed for the random number generator.
        a (int): The multiplier for the random number generator.
        c (int): The increment for the random number generator.
        m (int): The modulus for the random number generator.
        seen (set): A set of integers that have been generated.
        __state (dict): A dictionary representing the current state of the random number generator.
    """

    def __init__(self, seed: int, a: int, c: int, m: int) -> None:
        """Initializes the RNG object with the given parameters.

        Parameters:
        seed (int): The seed value for the RNG.
        a (int): The multiplier value for the RNG.
        c (int): The increment value for the RNG.
        m (int): The modulus value for the RNG.

        Raises:
        TypeError: If the seed parameter is not of type int.
        """
        # Validate the seed's type
        if isinstance(seed, int):
            self.seed = seed
        else:
            raise TypeError('Parameter "seed" must be of type int')

        # Initialize the set to keep track of the generated numbers. Sets are used to avoid duplicates.
        self.seen = set()

        # Initialize the internal state of the generator.
        self.__state = {"val": seed, "a": a, "c": c, "m": m}

    def __iter__(self):
        # Return self, as the __next__ method is implemented in the class.
        return self

    def __next__(self):
        """Returns the next random number in the sequence.

        Raises:
            StopIteration: If the generated number has been seen before.

        Returns:
            int: The next random number.
        """
        # Assign the state to a local variable
        state = self.__state

        # Generate the next random number using the linear congruential method
        state["val"] = (state["a"] * state["val"] + state["c"]) % state["m"]

        # If the number has been seen before, raise a StopIteration
        if state["val"] in self.seen:
            raise StopIteration()

        # Add the number to the set of seen numbers
        self.seen.add(state["val"])

        # Return the generated number
        return state["val"]

    def get_state(self) -> dict:
        """Returns a copy of the current state of the RNG.

        Returns:
            dict: A dictionary representing the current state of the RNG.
        """

        # Return a copy of the internal state so it cannot be mutated
        return self.__state.copy()

    def set_state(self, state: dict) -> None:
        """Sets the state of the RNG object.

        Args:
            state (dict): A dictionary containing the state of the RNG.
                Must include keys 'val', 'a', 'c', and 'm'.

        Raises:
            ValueError: If the dictionary is invalid and does not include
                the required keys.

        Returns:
            None
        """

        # Verify that the dictionary is valid and set the internal state
        if "val" in state and "a" in state and "c" in state and "m" in state:
            self.__state = state

            # Reset the set of seen numbers as if the generator has not been used
            self.seen.clear()
        else:
            raise ValueError("Invalid dictionary. Must include keys val, a, c, m")


class LaggedFibonacci:
    """Lagged Fibonacci random number generator.

    Attributes:
        seed (list[int]): The seed values used to initialize the generator.
        j (int): The value of j used in the generator.
        k (int): The value of k used in the generator.
        m (int): The value of m used in the generator.
    """

    def __init__(self, seed, j: int, k: int, m: int) -> None:
        """Initializes the LaggedFibonacci object.

        Args:
            seed (list[int]): The seed values used to initialize the generator.
            j (int): The value of j used in the generator.
            k (int): The value of k used in the generator.
            m (int): The value of m used in the generator.

        Raises:
            TypeError: If the seed is not a list of integers.
            ValueError: If the value of m is not an integer.
                        If the value of j is not greater than 0 and less than k.
                        If the length of k is not less than the length of the seed.
        """

        # Initialize the internal state of the generator to an empty dictionary
        self.__state = dict()

        # Validate the seed's type as well as the type of its elements
        if isinstance(seed, list) and all(isinstance(item, int) for item in seed):
            self.__state["val"] = seed
            self.seed = seed.copy()
        else:
            raise TypeError("Seed must be list of int")

        # Validate the value of m
        if isinstance(m, int):
            self.__state["m"] = m
        else:
            raise ValueError("Param M must be an integer")

        # Validate the value of j and k so that k is less than or equal to the length of the seed and j is greater than 0 and less than k
        if k <= len(seed):
            self.__state["k"] = k
            if j > 0 and j < k:
                self.__state["j"] = j
            else:
                raise ValueError("Param J must be greater than 0 and less than k")
        else:
            raise ValueError("Param k must be less than or equal to the length of seed")

    def __iter__(self):
        # Return self, as the __next__ method is implemented in the class.
        return self

    def __next__(self):
        """Generates the next random number.

        Returns:
            int: The next random number.

        Raises:
            StopIteration: If the generator has reached the initial seed state.
        """

        # Use negative indexing to find the values for k and j since we start from the right
        first_digit = self.__state["val"][-(self.__state["k"])]
        second_digit = self.__state["val"][-(self.__state["j"])]

        # Perform the lagged fibonacci operation to generate the next number
        number = (first_digit + second_digit) % self.__state["m"]

        # Shift the values in the list to the left by one
        self.__state["val"][:-1] = self.__state["val"][1:]
        self.__state["val"][-1] = number

        # If the generator has reached the initial seed state, raise a StopIteration
        if self.__state["val"] == self.seed:
            raise StopIteration()

        # Return the generated number
        return number

    def get_state(self) -> dict:
        """Returns a copy of the current state of the generator.

        Returns:
            dict: A dictionary representing the current state of the generator.
        """

        # Return a copy of the internal state so it cannot be mutated
        return self.__state.copy()

    def set_state(self, state: dict) -> None:
        """Sets the state of the generator using a dictionary.

        Args:
            state (dict): A dictionary representing the state of the generator.

        Raises:
            ValueError: If the dictionary does not include the required keys.
        """

        # Verify that the dictionary is valid and set the internal state
        if "val" in state and "j" in state and "k" in state and "m" in state:
            self.__state = state
            self.seed = state["val"]
        else:
            raise ValueError("Invalid dictionary. Must include keys val, j, k, m")


class Acorn:
    """Random number generator using the Acorn algorithm.

    Attributes:
        __state (dict): The internal state of the generator.
        start (list[int]): The initial seed values.
    """

    def __init__(self, seed: list[int], M: int) -> None:
        """Initializes the Acorn generator with a seed and modulus value.

        Args:
            seed (list[int]): The seed values for the generator.
            M (int): The modulus value.

        Raises:
            TypeError: If the seed is not a list of integers.
            ValueError: If the modulus value is not an integer.
        """

        # Initialize the internal state of the generator to an empty dictionary
        self.__state = dict()

        # Validate the seed's type as well as the type of its elements
        if isinstance(seed, list) and all(isinstance(item, int) for item in seed):
            self.__state["vals"] = seed
        else:
            raise TypeError("Seed must be list of int")

        # Validate the value of M
        if isinstance(M, int):
            self.__state["M"] = M
        else:
            raise ValueError("Param M must be an integer")

        # Set the initial seed values to compare later
        self.start = seed.copy()

    def __iter__(self):
        # Return self, as the __next__ method is implemented in the class.
        return self

    def __next__(self):
        """Generates the next random number in the sequence.

        Returns:
            list[int]: The next random number in the sequence.

        Raises:
            StopIteration: If the sequence has reached the initial seed values.
        """

        # Store the current state in a local variable
        state = self.__state

        # Create a new list to store the new values so that the original list is not mutated
        new_vals = state["vals"].copy()

        # Perform the Acorn algorithm to generate the next number
        for i in range(1, len(state["vals"])):
            # Set the new value to the sum of the previous value and the current value, modulo M starting at index 1 to avoid index out of range
            new_vals[i] = (new_vals[i - 1] + new_vals[i]) % state["M"]

        # If the sequence has reached the initial seed values, raise a StopIteration
        if new_vals == self.start:
            raise StopIteration()

        # Update the internal state with the new values
        state["vals"] = new_vals

        # Return the new values
        return new_vals

    def get_state(self) -> dict:
        """Returns a copy of the current state of the generator.

        Returns:
            dict: The current state of the generator.
        """

        # Return a copy of the internal state so it cannot be mutated
        return self.__state.copy()

    def set_state(self, state: dict) -> None:
        """Sets the state of the generator to the provided state dictionary.

        Args:
            state (dict): The state dictionary to set.

        Raises:
            ValueError: If the state dictionary is invalid and does not include the required keys.
        """

        # Verify that the dictionary is valid and set the internal state
        if "vals" in state and "M" in state:
            self.__state = state
            self.start = state["vals"]
        else:
            raise ValueError("Invalid dictionary. Must include keys vals, M")


class Analyzer:
    """Analyze random numbers generated by a random number generator.

    Attributes:
        rand_num_gen (object): The random number generator to analyze.
        max (int): The maximum value generated.
        min (int): The minimum value generated.
        average (float): The average value generated.
        period (int): The period of the generated numbers.
        bit_freqs (list[int]): The frequency of each bit in the generated numbers.
    """

    def __init__(self, rand_num_gen: object) -> None:
        """Initializes the Analyzer object.

        Args:
            rand_num_gen (object): The random number generator to analyze.
        """

        # Initialize the random number generator to analyze
        self.rand_num_gen = rand_num_gen

        # Initialize the maximum and minimum values to negative and positive infinity, respectively
        self.max = float("-inf")
        self.min = float("inf")

        # Initialize the average value to a float of 0
        self.average = 0.0

        # Initialize the period to 0
        self.period = 0

        # Initialize the bit frequencies to an empty list
        self.bit_freqs = []

    def analyze(self, max_nums=1e10):
        """Analyzes the random numbers generated by the random number generator.

        Args:
            max_nums (int, optional): The maximum number of random numbers to analyze. Defaults to 1e10.

        Returns:
            str: A message indicating the result of the analysis.
        """
        nums = []

        # Initialize the period and acorn flag to 0 and False, respectively
        acorn_period = 0
        is_acorn = False

        for num in self.rand_num_gen:
            # If the number of generated numbers is greater than or equal to the maximum number of numbers to analyze, break the loop
            if len(nums) >= max_nums:
                break

            try:
                # If num is an integer (rand_num_gen is not Acorn), append it to the list of numbers
                if isinstance(num, int):
                    nums.append(num)

                # If num is a list of integers (rand_num_gen is Acorn), set the acorn flag to True and increment the acorn period
                elif isinstance(num, list):
                    is_acorn = True
                    acorn_period += 1

                    # Append each integer in the list to the list of numbers (except the first one)
                    for i, j in enumerate(num):
                        # Validate that the number is an integer and not the first number in the list
                        if isinstance(j, int):
                            if i != 0:
                                nums.append(j)
                        else:
                            raise TypeError()
                else:
                    raise TypeError()
            except TypeError:
                return "Random number generator must return int or list[int]"

        # If no valid numbers were found, raise a ValueError
        if not nums:
            raise ValueError("No valid numbers found.")

        # Set the maximum, minimum, and average values
        self.max = max(nums)
        self.min = min(nums)
        self.average = sum(nums) / len(nums) if len(nums) > 0 else 0

        # Set the period to the length of the list of numbers if the generator is not Acorn, otherwise set it to the acorn period
        self.period = len(nums) if not is_acorn else acorn_period

        # Set the length of the bit frequencies list to the bit length of the maximum number
        bit_length = self.max.bit_length()

        # Initialize the bit frequencies list to a list of zeros with a length of the bit length
        self.bit_freqs = [0 for _ in range(bit_length)]

        # Iterate over the numbers and update the bit frequencies
        for num in nums:
            # Convert the number to binary and zero-fill (left-pad) it to the bit length
            temp = bin(num)[2:].zfill(bit_length)

            # Convert the string to a list of characters using the spread operator and reverse it so that the least significant bit is at index 0
            temp = [*temp][::-1]

            # Update the bit frequencies
            for i, j in enumerate(temp):
                if j == "1":
                    self.bit_freqs[i] += 1


# Below is an example of how to use the classes and methods above to generate random numbers and analyze them.

# ===========================================================
# =+==+++++===+++++===== Example Usage =====+++++===+++++==+=
# ===========================================================

# Initialize the seeds and parameters for the random number generators
ms_seed = 17628322
lcg_seed = 2932
lcg_a = 21
lcg_c = 55
lcg_m = 359828
lf_seed = [31, 42, 46, 98, 63, 21, 99, 83, 72, 75, 12]
lf_j = 4
lf_k = 8
lf_m = 100
ac_seed = [2, 3, 4, 5, 6]
ac_M = 178

# Initialize the random number generators
ms = MiddleSquare(ms_seed)
lcg = LinearCongruential(lcg_seed, lcg_a, lcg_c, lcg_m)
lf = LaggedFibonacci(lf_seed, lf_j, lf_k, lf_m)
ac = Acorn(ac_seed, ac_M)

# Initialize the analyzers with the random number generators
ms_analyzer = Analyzer(ms)
lcg_analyzer = Analyzer(lcg)
lf_analyzer = Analyzer(lf)
ac_analyzer = Analyzer(ac)

# Analyze the random number generators
ms_analyzer.analyze()
print(ms_analyzer.max)
print(ms_analyzer.min)
print(ms_analyzer.average)
print(ms_analyzer.period)
print(ms_analyzer.bit_freqs)
print("=======")
lcg_analyzer.analyze()
print(lcg_analyzer.max)
print(lcg_analyzer.min)
print(lcg_analyzer.average)
print(lcg_analyzer.period)
print(lcg_analyzer.bit_freqs)
print("=======")
lf_analyzer.analyze()
print(lf_analyzer.max)
print(lf_analyzer.min)
print(lf_analyzer.average)
print(lf_analyzer.period)
print(lf_analyzer.bit_freqs)
print("=======")
ac_analyzer.analyze()
print(ac_analyzer.max)
print(ac_analyzer.min)
print(ac_analyzer.average)
print(ac_analyzer.period)
print(ac_analyzer.bit_freqs)
