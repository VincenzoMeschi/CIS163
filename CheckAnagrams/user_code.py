"""
A string is an anagram of another string if it can be formed by rearranging the characters in the first string (using all of the characters exactly the number of times they occur in the first string).

For instance,

    Example 1: 'act' and 'cat' are anagrams
    Example 2: 'state' and 'taste' are anagrams
    Example 3: 'states' and 'taste' are not anagrams as 'states' has two 's' characters but 'taste' only has one 's'

Your task is to create a function that excepts two strings and returns True if they are anagrams and False if they are not anagrams of one another. The function skeleton is already provided in the code box below.

Note, you are welcome to have other code to test your function. Your function will be called many times behind the scenes to verify it works correctly with a variety of inputs

Your code snippet should define the following variables:


Name 	Type 	Description
check_anagram 	function 	function to check if two strings are anagrams
"""


def check_anagram(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False

    book = {}
    word1, word2 = set(word1), set(word2)

    for letter in word1:
        book[letter] = 0

    for letter in word2:
        book[letter] += 1

    for val in book:
        if book[val] != 1:
            return False

    return True
