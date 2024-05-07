#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    result=0
    a_dict=dict()
    b_dict=dict()

    for c in string.ascii_lowercase:
        a_dict[c]=0
        b_dict[c]=0
    for c in a:
        a_dict[c] = a_dict[c] + 1
    for c in b:
        b_dict[c] = b_dict[c] + 1
    for c in string.ascii_lowercase:
        result += abs(a_dict[c] - b_dict[c])
    return result


# test cases
if __name__ == '__main__':

    # test 1
    a='cde'
    b='abc'
    print("Test 1 (4):", makeAnagram(a,b))