from typing import List
# Write any import statements here
import random
import timeit

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    # Write your code here
    result=0
    hist=set()
    oldest=D[0]

    # keep track of eaten dishes using history set.  skip counting if D[n] in history set.
    for n in range(0, N):
        if D[n] in hist:
            continue
        result+=1
        hist.add(D[n])
        if len(hist)>K:
            for i in hist:
                oldest = i
                break
            hist.remove(oldest)

    return result


# Test cases
if __name__ == '__main__':

    # Test 1
    N=6
    D=[1,2,3,3,2,1]
    K=1
    print("Test 1:", getMaximumEatenDishCount(N,D,K))

    # Test 2
    N=6
    D=[1,2,3,3,2,1]
    K=2
    print("Test 2:", getMaximumEatenDishCount(N,D,K))

    # Test 3
    N=7
    D=[1,2,1,2,1,2,1]
    K=2
    print("Test 3:", getMaximumEatenDishCount(N,D,K))
