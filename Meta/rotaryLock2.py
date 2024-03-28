from typing import List
# Write any import statements here
import timeit
import random

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    # Write your code here
    def minMoveTime(source: int, target: int, N1: int) -> int:
        diff = abs(source-target)
        if diff > int(N1 / 2):
            return N1-diff
        else:
            return diff

    result=minMoveTime(1,C[0],N)
    lock1=C[0]
    lock2=1
    for i in range(1, M):
        print(lock1, lock2, result)
        min1=minMoveTime(lock1,C[i],N)
        min2=minMoveTime(lock2,C[i],N)
        if min1 <= min2:
            result+=min1
            lock1=C[i]
        else:
            result+=min2
            lock2=C[i]
    print(lock1, lock2, result)

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
    #ans: 9
    N3=10
    M3=10
    C3=[1,9,2,8,3,7,4,6,5,5]
    #ans: ??
    N4=100
    M4=10
    C4=[]
    for i in range(0,N4):
        C4.append(random.choice(range(1,N4+1)))

    start = timeit.default_timer()
    print("result:", getMinCodeEntryTime(N3,M3,C3))
    stop = timeit.default_timer()
    print("runtime (secs):", stop-start)