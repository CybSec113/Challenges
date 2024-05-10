#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY stringList
#  2. STRING_ARRAY queries
#

def matchingStrings(stringList, queries):
    # Write your code here
    result = [0] * len(queries)
    count = dict()

    for i in stringList:
        if i in count:
            count[i] = count[i] + 1
        else:
            count[i] = 1

    for i in range(len(queries)):
        if queries[i] in count:
            result[i] = count[queries[i]]
        else:
            result[i] = 0

    return result

# test cases
if __name__ == '__main__':

    #test 1
    a=['aba','baba','aba','xzxb']
    b=['aba','xzxb','ab']
    print("Test 1 (2,1,0):", matchingStrings(a,b))
