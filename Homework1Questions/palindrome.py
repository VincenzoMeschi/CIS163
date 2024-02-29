# Palindrome

# A palindrome is a word that reads the same forward and backwards. For instance, racecar is a palindrome.
# Your Task

# Using recursion, implement the function below called check_palindrome that takes in a string and returns a boolean, True if it is a palindrome, otherwise False.


def check_palindrome(string: str) -> bool:
    if len(string) == 1:
        return True
    elif len(string) == 2:
        if string[0] == string[1]:
            return True
        return False

    return string[0] == string[-1] and check_palindrome(string[1:-1])
