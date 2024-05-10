import math
import os
import random
import re

def findSubstrings(s):
    # Write your code here

    result=set()
    for i in range(len(s)):
        a=s[i]
        for j in range(i+1, len(s)):
            if s[j] not in a:
                a += s[j]
                result.add(a)
            
    return len(result) + len(s)

if __name__ == '__main__':
    s='bcada'
    print("result (12):", findSubstrings(s))