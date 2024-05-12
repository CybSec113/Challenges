#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

# can only capitalize letters in a or delete lowercase letters from a.
# return YES if we can get a to match b, otherwise, return NO
# a is [a-z,A-Z], b is only uppercase [A-Z]
# contraints: 1 >= q <= 10 # max number of queries per input file
#             1 <= |a|,|b| <= 1000

def abbreviation(a, b):
    # Write your code here

    # if b > a, can't match
    if len(b) > len(a):
        return "NO"

    # result: a-cols, b-rows
    result = [ [0]*len(a) for i in range(len(b)) ]
    result[0][0] = a[0].upper() == b[0]
    for i in range(len(b)):
        for j in range(1, len(a)):
            if i==0: # initialize first row
                if result[i][j-1]:
                    result[i][j] = a[j].islower()
                else:
                    result[i][j] = a[j].upper()==b[i]
                continue
            if j<i: # must compare against substr of a at least as long as substr of b
                result[i][j] = False
                continue
            if i>0:  # the general case
                result[i][j] = (result[i][j-1] and a[j].islower()) or (result[i-1][j-1] and a[j].upper()==b[i])
            
    
    for i in range(len(b)):
        for j in range(len(a)):
            if result[i][j] == True:
                print("Y", end=' - ')
            else:
                print("N", end=' - ')
        print("")

    if result[-1][-1] == True:
        return "YES"
    else: return "NO"

# test cases
if __name__ == '__main__':

    # test 0
    a = 'bCAdbe'
    b = 'AB'
    print("Test 0 (Y): ",abbreviation(a,b))

    # test 1
    a = 'daBcd'
    b = 'ABC'
    print("Test 1 (Y): ",abbreviation(a,b))

    # test 2
    a = 'AbcDE'
    b = 'ABDE'
    print("Test 2 (Y): ",abbreviation(a,b))

    # test 3
    a = 'AbcDE'
    b = 'AFDE'
    print("Test 3 (N): ",abbreviation(a,b))

    # test 4
    a = 'KXzQ'
    b = 'K'
    print("Test 4 (N): ",abbreviation(a,b))
