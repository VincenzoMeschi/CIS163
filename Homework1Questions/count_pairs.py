# Pairs

# Given a string, we'll assume a pair is any two characters repeated in a row. The same character repeated 3 times in a row then counts as two pairs (pairs can overlap).
# Your Task

# Using recursion, implement the function below called count that counts the number of pairs in the string. For example, the string "AAABCBB" contains 3 pairs.


def count(string):
    if len(string) < 2:
        return 0

    if string[0] == string[1]:
        return 1 + count(string[1:])
    return count(string[1:])
