"""
 lab1.2. Compute Sum of Sorted Subsequence with Maximum Sum

Consider a list such as: [1,2,4,1,6,8,2,3,5,4,9]

We wish to identify the sum of the numbers in the contiguous subsequence of the list that is in non-decreasing order which produces the maximum sum.

Specifically, the above list has multiple contiguous subsequences that are sorted in ascending order, and for each of them we can get their respective sums. In our case, this gives:

    1,2,4 which sums to 7
    1,6,8 which sums to 15
    2,3,5 which sums to 10
    4,9 which sums to 13

Note, that 1,2 is also a subsequence in ascending order, but because it is part of a larger subsequence that is sorted in ascending order, we don't bother considering it (because we know it is not maximal so long as the numbers of positive).

Your task is to create a function that accepts a list and returns the maximum sum of the elements in any contiguous subsequence that are sorted in ascending order (e.g. non-decreasing subsequence)

Note, you are welcome to have other code to test your function. Your function will be called many times behind the scenes to verify it works correctly with a variety of inputs

Your code snippet should define the following variables:


Name 	Type 	Description
max_sum_sorted_subseq 	function 	function to compute max sum of sorted subsequence
"""
# [1,2,3,4,5,6,7,8]


def max_sum_sorted_subseq(lst):
    if len(lst) > 1:
        totalSum = 0
        tempSum = lst[0]

        pointA = 1

        while pointA < len(lst):
            if lst[pointA] > lst[pointA - 1]:
                tempSum += lst[pointA]
            else:
                totalSum = max(totalSum, tempSum)
                tempSum = lst[pointA]
            pointA += 1

        return max(totalSum, tempSum)
    elif len(lst) == 1:
        return lst[0]
    else:
        return 0


print(max_sum_sorted_subseq([3, 4, 6, 25, 2, 20, 23]))
