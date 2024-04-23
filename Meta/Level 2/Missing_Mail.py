# You are the manager of a mail room which is frequently subject to theft. 
# A period of NN days is about to occur, such that on the iith day, the following 
# sequence of events will occur in order:
# 
#     1. A package with a value of ViVi​ dollars will get delivered to the mail room 
#         (unless Vi=0Vi​=0, in which case no package will get delivered).
#     2. You can choose to pay CC dollars to enter the mail room and collect all of the 
#         packages there (removing them from the room), and then leave the room
#     3. With probability SS, all packages currently in the mail room will get stolen 
#         (and therefore removed from the room).
# 
# Note that you're aware of the delivery schedule V1..NV1..N​, but can only observe the state of the 
# mail room when you choose to enter it, meaning that you won't immediately be aware of whether or 
# not packages were stolen at the end of any given day.
# 
# Your profit after the NNth day will be equal to the total value of all packages which you collected 
# up to that point, minus the total amount of money you spent on entering the mail room.
# 
# Please determine the maximum expected profit you can achieve (in dollars).
# 
# Note: Your return value must have an absolute or relative error of at most 10−610−6 to be considered correct.
# 
# Constraints
# 1 ≤ N ≤ 4,000
# 0 ≤ Vi ≤ 1,000
# 1 ≤ C ≤ 1,000
# 0.0 ≤ S ≤ 1.0
# 

from typing import List
# Write any import statements here

def getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:
    # Write your code here

    # edge case
    if S == 0.0:
        return sum(V)-C

    result=0.0      # keep track of return value
    entries=0       # keep track of entries and adjust return value before returning result
    expret=0.0      # Keep track of running expected return value.  If expret > C, then enter room
    for i in V:
        if i >= C:
            if expret > 0.0:
                result+=expret+i*(1.0-S)+i*(1.0-S)
            else:
                result+=i
            expret=0.0
            entries+=1
            continue
        expret+=i*(1.0-S)
        if expret >= C:
            result+=expret
            entries+=1
            expret=0.0
            continue

    result-=entries*C
    return result


# Test cases
if __name__ == '__main__':
    # Test 1
    N=5
    V=[10,2,8,6,4]
    C=5
    S=0.0
    print("Test 1 (25.0000000):", getMaxExpectedProfit(N,V,C,S))

    # Test 2
    N=5
    V=[10,2,8,6,4]
    C=5
    S=1.0
    print("Test 2 (9.00000000):", getMaxExpectedProfit(N,V,C,S))

    # Test 3
    N=5
    V=[10,2,8,6,4]
    C=3
    S=0.5
    print("Test 3 (17.0000000):", getMaxExpectedProfit(N,V,C,S))

    # Test 4
    N=5
    V=[10,2,8,6,4]
    C=3
    S=0.15
    print("Test 4 (20.1082500):", getMaxExpectedProfit(N,V,C,S))
