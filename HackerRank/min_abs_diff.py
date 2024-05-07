#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Write your code here
    result=(10**9)+1

    # sorting the array gets all the biggest pairs together, avoiding nested looping accross all possible pairs.
    arr.sort()
    for i in range(len(arr)-1):
        if abs(arr[i]-arr[i+1]) < result:
            result = abs(arr[i]-arr[i+1])

    return result

# test cases
if __name__ == '__main__':

    # test 1
    arr=[-59,-36,-13,1,-53,-92,-2,-96,-54,75]
    print("Test 1 (1):", minimumAbsoluteDifference(arr))

    # test 2
    arr=[1,-2,71,68,17]
    print("Test 2 (3):", minimumAbsoluteDifference(arr))
