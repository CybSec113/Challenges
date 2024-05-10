#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'whatFlavors' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money
#

def whatFlavors(cost, money):
    # Write your code here
    count = dict()
    for i in cost:
        if i in count:
            count[i] = count[i] + 1
        else:
            count[i] = 1
    
    for i in range(len(cost)):
        diff = money - cost[i]
        if diff in count:
            if diff == cost[i] and count[diff] == 1:
                continue
            elif diff == cost[i]:
                print(i+1, cost.index(diff, i+1)+1)
            else:
                print(i+1, cost.index(diff)+1)
            return

# test cases
if __name__ == '__main__':

    # test 1
    money = 4
    n=5
    cost=[1,4,5,3,2]
    print("Test 1(1 4):")
    whatFlavors(cost, money)

    # test 2
    money = 4
    n=4
    cost=[2,2,4,3]
    print("Test 2(1 2):")
    whatFlavors(cost, money)

    # test 2
    money = 8
    n=5
    cost=[4,3,2,5,7]
    print("Test 3(2 4):")
    whatFlavors(cost, money)
