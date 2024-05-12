#!/bin/python3

import math
import os
import random
import re
import sys

# DYNAMIC PROGRAMMING!!
# Given an array of integers, find the subset of non-adjacent 
# elements with the maximum sum. Calculate the sum of that subset. 
# It is possible that the maximum sum is 0, the case when all elements are negative. 

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    result = [0] * (len(arr)+1)
    result[0] = 0
    result[1] = max(0, arr[0])
    for i in range(2,len(arr)+1):
        result[i] = max(result[i-1], result[i-2] + arr[i-1])

    return result[-1]

# test cases
if __name__ == '__main__':

    # Test 0 
    arr = [1,2,3,4,5,6,7,8,9]
    print("Test 0:", maxSubsetSum(arr))

    # Test 1 (8)
    arr = [-2,1,3,-4,5]
    print("Test 1 (8):", maxSubsetSum(arr))

    # Test 2 (0)
    arr = [-2,-3,-1]
    print("Test 2 (0):", maxSubsetSum(arr))

    # Test 3 (13)
    arr = [3,7,4,6,5]
    print("Test 3 (13):", maxSubsetSum(arr))

    # Test 4 (11)
    arr = [2,1,5,8,4]
    print("Test 4 (11):", maxSubsetSum(arr))

    # Test 5 (15)
    arr = [3,5,-7,8,10]
    print("Test 5 (15):", maxSubsetSum(arr))
