# Scoreboard Interference (Chapter 1)

# You are spectating a programming contest with NN competitors, 
# each trying to independently solve the same set of programming 
# problems. Each problem has a point value, which is either 1 or 2.
# On the scoreboard, you observe that the iith competitor has attained 
# a score of SiSi​, which is a positive integer equal to the sum of 
# the point values of all the problems they have solved.
# The scoreboard does not display the number of problems 
# in the contest, nor their point values. Using the information 
# available, you would like to determine the minimum possible number of 
# problems in the contest.

# Constraints:
# 1 <= N <= 500,000
# 1 <= S[i] <= 1,000,000,000

from typing import List
# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
    # Write your code here
    ones, twos=0,0
    for i in range(N):
        twos=max(twos,S[i]//2)
        ones=max(ones,S[i]%2)

    return ones+twos

# Test Cases
if __name__ == '__main__':

    #Test 1: 4, [1,1,2,2]
    N=6
    S=[1,2,3,4,5,6]
    print("Test 1:", getMinProblemCount(N,S))
    
    #Test 2: 3, [1,1,2]
    N=4
    S=[4,3,3,4]
    print("Test 2:", getMinProblemCount(N,S))

    #Test 3: 4, [2,2,2,2]
    N=4
    S=[2,4,6,8]
    print("Test 3:", getMinProblemCount(N,S))
    