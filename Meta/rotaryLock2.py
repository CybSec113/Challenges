from typing import List
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    # Write your code here

    #returns smallest distance from current lock number (e.g., source) to target
    def minMoveTime(source: int, target: int):
        diff=0
        if source-target > 0:
            diff=source-target
        else: diff=target-source
        return min(diff, N-diff)

    # need to rethink this approach using dynamic programming
    # prior approach was 'greedy' and sub-optimal

    return result

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