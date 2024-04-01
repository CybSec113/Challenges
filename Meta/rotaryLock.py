from typing import List
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    # Write your code here

    #returns smallest distance from current lock number (e.g., source) to target
    def minMoveTime(source: int, target: int, N1: int) -> int:
        diff = abs(source-target)
        if diff > int(N1 / 2):
            return N1-diff
        else:
            return diff

    result=0
    #iterate over each int in C and add smalles distance to next target
    for i in range(0, len(C)):
        if i==0:
            result+=minMoveTime(1,C[0],N)
        else:
            result+=minMoveTime(C[i-1],C[i],N)

    return result


# Test Cases
if __name__ == '__main__':

    #Test 1: 2
    N=3
    M=3
    C=[1,2,3]
    print("Test 1", getMinCodeEntryTime(N,M,C))

    #Test 2: 11
    N=10
    M=4
    C=[9,4,4,8]
    print("Test 2", getMinCodeEntryTime(N,M,C))
