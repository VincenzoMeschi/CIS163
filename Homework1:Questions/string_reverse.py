# Your Task

# Using recursion, implement the function below called reverse that takes in a string and returns the reversed string.

# For example, the string "hello" reversed is "olleh".


def reverse(word):
    if len(word) == 1:
        return word

    return word[-1] + reverse(word[:-1])
