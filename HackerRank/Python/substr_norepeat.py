import math
import os
import random
import re
import itertools

# for a given string, find all substrings without repeating characters
# for example, aba: a, b, a, ab, ba, aba (note: substring of length 1 is always unique)
# PENDING CORRECT SOLUTION

def findSubstrings(s):
    # Write your code here
    result=set()
    subsets=list()

    for i in range(2, len(s)):
        subsets += list(itertools.combinations(range(len(s)), i))

    for i in subsets:
        a=s[i[0]]
        for j in i:
            if s[j] not in a:
                a+=s[j]
                result.add(a)

    print(sorted(result))
    return len(result)

# test cases
if __name__ == '__main__':

    # test 1
    s='bcada'
    print("Test 1 (12):", findSubstrings(s))

    # test 2
    s='aaaaa'
    print("Test 2 (5):", findSubstrings(s))

    # test 3
    # a, b, c, d, e, ab, ac, ad, ae, bc, bd, be, cd, ce, de, abc, abd, abe, bcd, bce, cde, abcd, acde, bcde, abcde
    s='abcde'
    print("Test 3 (32):", findSubstrings(s))
