"""
 lab1.3. Most Common Element in List

Consider a list of integers such as: [1,2,1,2,9,9,8,2,2]

We wish to identify the most common element in the list. For the example above,

    1 occurs twice
    2 occurs four times
    8 occurs once
    9 occurs twice

so, the most common element is 2.

Your task is to create a function that accepts a list and returns the most common element. In the case of a tie, where there are multiple integers that occur the same (maximal) number of times, return the larges of the elements that occurs the most often.

Note, you are welcome to have other code to test your function. Your function will be called many times behind the scenes to verify it works correctly with a variety of inputs

Your code snippet should define the following variables:
Name 	Type 	Description
most_common_element 	function 	function to determine most common element
"""


def most_common_element(lst):
    counter = {}
    max_count = 0
    result = lst[0]

    for num in lst:
        counter[num] = counter.get(num, 0) + 1
        if counter[num] > max_count or (counter[num] == max_count and num > result):
            max_count = counter[num]
            result = num

    return result
