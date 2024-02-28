# String Modification

# Given two strings, consider whether it is possible to turn the first string into the second string by only removing letters (without rearranging or adding any letters).
# Your Task

# Using recursion, implement can_reach function to determine whether it is possible to modify original by only removing letters to reach target. You will probably want a helper function.
# Example

# Consider the string "designation". It is not possible to reach a "hat" from this string (would need to add an "h"). However, it is possible to reach "sat".


def can_reach(original: str, target: str) -> bool:
    if len(original) < len(target):
        return False
    if len(target) == 0:
        return True
    if original[0] == target[0]:
        return can_reach(original[1:], target[1:])
    return can_reach(original[1:], target)



