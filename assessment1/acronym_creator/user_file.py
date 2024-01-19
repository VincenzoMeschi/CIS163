"""
Acronym Creator

Acronyms are commonly created from a series of words by taking the first letter of each "important" word and combining them together. One common way of distinguising important from non-important words is by deciding that the important words are the ones that are capitalized, and the non-important words, like "of" are not capitalized.
Example

Consider the string "Charity for the Polar Bears and other Arctic Animals". In this string, "Charity", "Polar", "Bears", "Arctic", "Animals" are the important words as they are capitalized, whereas "for", "the", "and", "other" are the non-important words since they are not capitalized. Combining the first letter of the important words gives the acronym "CPBAA".
Example 2

The string "Grand Valley State University School of Computing Club" should give "GVSUSCC".
Your Task

Implement the function below called acronym_creator that takes in a string of multiple "important" (capitalized) and "non-important" (not capitalized) words. From this string, create a string containing the acronym obtained by combining, in order, the first letter of each of the "important" words. Return this string which is the acronym.

Your code snippet should define the following variables:
"""


def acronym_creator(str1):
    temp = str1.split(" ")
    total = ""
    for word in temp:
        if ord(word[0]) >= 65 and ord(word[0]) <= 90:
            total += word[0]

    return total


print(acronym_creator("Grand Valley State Computing club Of the World"))
# 65 - 90
    