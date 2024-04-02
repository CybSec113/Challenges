# There's a stack of NN inflatable discs, with the iith disc from the top 
# having an initial radius of Ri, inches.
# 
# The stack is considered unstable if it includes at least one disc whose 
# radius is larger than or equal to that of the disc directly under it. 
# In other words, for the stack to be stable, each disc must have a strictly 
# smaller radius than that of the disc directly under it.
# 
# As long as the stack is unstable, you can repeatedly choose any disc of your 
# choice and deflate it down to have a radius of your choice which is strictly 
# smaller than the disc’s prior radius. The new radius must be a positive integer number of inches.
# 
# Determine the minimum number of discs which need to be deflated in order to make the stack stable, 
# if this is possible at all. If it is impossible to stabilize the stack, return −1 instead.
# 
# Constraints
# 1 ≤ N ≤ 50
# 1 ≤ Ri ≤ 1,000,000,000
#

from typing import List
# Write any import statements here

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
    # Write your code here
    if N==1:
        return 0

    result=0
    for i in range(N-1,0,-1):
        if R[i-1] >= R[i]:
            if R[i] - 1 > 0:
                R[i-1] = R[i] - 1
                result+=1
            elif R[i] - 1 == 0:
                result=-1
                break

    return result

# Test cases
if __name__ == '__main__':
    # Test 1
    N=5
    R=[2,5,3,6,5]
    print("Test 1 (3):", getMinimumDeflatedDiscCount(N,R))

    # Test 2
    N=3
    R=[100,100,100]
    print("Test 2 (2):", getMinimumDeflatedDiscCount(N,R))

    # Test 3
    N=4
    R=[6,5,4,3]
    print("Test 3 (-1):", getMinimumDeflatedDiscCount(N,R))
