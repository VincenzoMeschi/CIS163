# recursive function to remove vowels from a string
def devowel(string: str) -> str:
    def is_vowel(letter: str) -> bool:
        vowels = ["a", "e", "i", "o", "u"]
        if letter.lower() in vowels:
            return True
        return False

    if len(string) == 1:
        if is_vowel(string):
            return ""
        return string

    if is_vowel(string[0]):
        return devowel(string[1:])
    return string[0] + devowel(string[1:])


def add_asterisks(string: str) -> str:
    if len(string) == 1:
        return string

    return string[0] + "*" + add_asterisks(string[1:])


print(add_asterisks("allStar"))


def remove_dupe(string: str) -> str:
    if len(string) == 1:
        return string

    if string[0] == string[1]:
        return string[0] + remove_dupe(string[2:])

    return string[0] + remove_dupe(string[1:])


print(remove_dupe("allStar"))


def triangle(num_rows: int):
    if num_rows == 1:
        return 1
    elif num_rows < 1:
        raise ValueError("Num rows must be greater than 0")
    return num_rows + triangle(num_rows - 1)


print(triangle(5))
