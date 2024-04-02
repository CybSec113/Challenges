#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
# A left rotation operation on an array shifts each of the array's elements unit to the left. 
# For example, if left rotations are performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2]
# 
# Note that the lowest index item moves to the highest index in a rotation. 
# This is called a circular array.
# 
# Given an array a of n integers and a number, d, perform d left rotations on the array. 
# Return the updated array to be printed as a single line of space-separated integers.
# 
# Function Description
# Complete the function rotLeft in the editor below.
# rotLeft has the following parameter(s):
#   int a[n]: the array to rotate
#   int d: the number of rotations
# Returns
#   int a'[n]: the rotated array
# 
# Input Format
# The first line contains two space-separated integers n
# and d, the size of a, and the number of left rotations.
# The second line contains n space-separated integers, each an a[i].

def rotLeft(a, d):
    # Write your code here

    return a[d:]+a[0:d]


# test cases
if __name__ == '__main__':

    # test 1
    d=4
    a=[1,2,3,4,5]
    print("Test 1:", rotLeft(a,d))
