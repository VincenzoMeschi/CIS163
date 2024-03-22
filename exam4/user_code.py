# English Beggars
# The English take standing in line very seriously. This is so deeply ingrained into English culture that given a pile of coins, beggars will take turns taking one coins from the pile one at a time.

# For example, given the following pile represented as a list [1, 2, 3, 4, 5], the two beggars will take from the pile one at a time. Beggar one will establish a list of coins of [1, 3, 5] and beggar two will establish a list of coins of [2, 4]. Therefore the list you would return would be [9, 6].

# The same list split between three beggars would return [5, 7, 3].

# It should be noted that not every beggar will get an equal amount of turns. Therefore one can assume that not every list of coins will be evenly distributed amongst each beggar.

# Your Task
# Complete the helper function to help determine how much money each beggar receives from the pile of coins in total as a list.
# In the beggars function, please select one of the lists to use and uncomment it.
# It may be in your best interest to create a helper function
# You must use recursion.
# You may use one additional loop if you need to sum the elements of your final list
# BE SURE TO DELETE ALL COMMENTS IN YOUR SUBMISSION!!!
# Your code snippet should define the following variables:


def beggars(vals: list, n: int) -> list:  
    if n == 0:
        return []
    
    return divvy(vals, n)

def divvy(values, beggars_count, current_beggar=0, results=None):
        if results is None:
            results = [0] * beggars_count
        
        if not values:
            return results
        
        results[current_beggar] += values[0]
        
        next_beggar = (current_beggar + 1) % beggars_count
        
        return divvy(values[1:], beggars_count, next_beggar, results)

# Testing the corrected function




# Squares Needed
# A king asks a young man how he wants to be rewarded. The young man asks the king to bring out a chess board (to everyone's horror). The young man asks to be compensated with only 1 grain of rice for the first square, 2 grains for the second, 4 for the third, 8 for the fourth and so on, always doubling the previous.

# Your Task
# Complete the function to calculate how squares are needed to compensate for the number of grains given as the target.
# You cannot use a for loop and your solution must be recursive.
# If you feel necessary (though not required) you may use a helper function.
# Your code snippet should define the following variables:

def squares_needed(grains: int) -> int:
    if grains == 0:
        return 0
    if grains == 1:
        return 1
    return 1 + squares_needed(grains // 2)


# Culling Zombies
# You are a survivor of the zombie apocalypse. You are a member of what others refer to as the clearence crew. The clearence crew goes around and takes out hordes of zombies in a given area.

# Your Task
# Complete the function to calculate how many days it would take for the clearence crew to the area's zombie population to zero.
# You cannot use loops.
# Your solution must be recursive.
# Your code snippet should define the following variables:

# result for people=5 eliminate=2 zombies=25 is incorrect
# Expected: 3
# Actual: 9

# result for people=3 eliminate=1 zombies=9 is incorrect
# Expected: 3
# Actual: 5

def cull_zombies(people: int, eliminate: int, zombies: int) -> int:
    if zombies <= 0:
        return 0
    return 1 + cull_zombies(people, eliminate, zombies - people * eliminate)