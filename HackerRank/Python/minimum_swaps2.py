#!/bin/python3

import math
import os
import random
import re
import sys

# You are given an unordered array consisting of consecutive integers 
# [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any 
# two elements. 
# Find the minimum number of swaps required to sort the array in ascending order. 

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    result = 0

    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    i=0
    while i < len(arr):
        if arr[i] == i+1:
            i+=1
        else:
            swap(i, arr[i]-1)
            result += 1

    return result

# test cases
if __name__ == '__main__':

    # Test 0
    arr = [2,1]
    print("Test 0: ", minimumSwaps(arr))

    # Test 1 (5)
    arr = [7,1,3,2,4,5,6]
    print("Test 1 (5):", minimumSwaps(arr))

    # Test 2 (3)
    arr = [4,3,1,2]
    print("Test 2 (3):", minimumSwaps(arr))

    # Test 3 (3)
    arr = [2,3,4,1,5]
    print("Test 3 (3):", minimumSwaps(arr))

    # Test 4 (3)
    arr = [1,3,5,2,4,6,7]
    print("Test 4 (3):", minimumSwaps(arr))

