from typing import List
# Write any import statements here
import timeit
import random
import math

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    # Write your code here
    def minMoveTime(source: int, target: int, N1: int) -> int:
        diff = abs(source-target)
        if diff >= math.ceil(N1/2):
            return N1-diff
        else:
            return diff

    result=0
    lock1=1
    lock2=1
    for i in range(0, M):
        print("i ===> ", i, C[i])
        min1=minMoveTime(lock1,C[i],N)
        min2=minMoveTime(lock2,C[i],N)
        #print("mins", min1, min2)
        if min1 <= min2:
            result+=min1
            lock1=C[i]
        else:
            result+=min2
            lock2=C[i]
        print("locks", lock1, lock2, result)
        print()

    return result


if __name__ == '__main__':
    #ans: 2
    N1=3
    M1=3
    C1=[1,2,3]
    #ans: 11
    N2=10
    M2=4
    C2=[9,4,4,8]
    #ans: 8
    N3=97
    M3=2
    #C3=[90,30,32,25,2,4,19,86,1,26]
    C3=[1,50]
    #ans: ??
    N4=99
    M4=10
    C4=[]
    for i in range(0,M4):
        C4.append(random.choice(range(1,N4+1)))

    print(C3)
    start = timeit.default_timer()
    print("result:", getMinCodeEntryTime(N3,M3,C3))
    stop = timeit.default_timer()
    print("runtime (secs):", stop-start)