"""
Jerigonza

Jerigonza is a Spanish language game played by children where children speak in essentially gibberish. It's similar to Pig Latin in English, just with a different set of rules.

The rules for Jerigonza is that whenever there is a vowel, you add the letter "p" after the vowel, and then repeat the vowel.
Examples:

    the name "carlos" would be "caparlopos"
    the string "feliz" would be "fepelipiz"

Your Task

Implement the function below called jerigonza that takes in a string representing a word and returns a string of the word in Jerigonza.

You can assume that your string will be a single word in all lowercase. The string will contain only the letters a-z (with no special accents).

Your code snippet should define the following variables:
"""

def jerigonza(word: str) -> str:
    vowels = {"a", "e", "i", "o", "u"}
    temp = ""

    for letter in word:
        temp += letter
        if letter in vowels:
            temp += "p" + letter

    return temp

# you can put other code here if you want
