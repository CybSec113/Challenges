from typing import List
# Write any import statements here
import timeit

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    # Write your code here
    def minMoveTime(source: int, target: int, N1: int) -> int:
        diff = abs(source-target)
        if diff > int(N1 / 2):
            return N1-diff
        else:
            return diff

    result=0
    for i in range(0, len(C)):
        if i==0:
            result+=minMoveTime(1,C[0],N)
        else:
            result+=minMoveTime(C[i-1],C[i],N)

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

    start = timeit.default_timer()
    print("result:", getMinCodeEntryTime(N2,M2,C2))
    stop = timeit.default_timer()
    print("runtime (secs):", stop-start)