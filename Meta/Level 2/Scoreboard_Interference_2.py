# Scoreboard Interference (Chapter 1)

# You are spectating a programming contest with NN competitors, 
# each trying to independently solve the same set of programming 
# problems. Each problem has a point value, which is either 1,2, or 3.
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
    max_score=max(S)
    ones, twos, threes=0,0,0

    # any score will have remainder 0, 1, 2 in mod 3
    # so, only need one problem each of 1 and 2 to make any score
    # so, need to keep track if there are scores that need a 1 or a 2
    # e.g., 1%3 = 1, 2%3 = 2
    for s in S:
        threes=max(threes,s//3)
        if s % 3 == 2:
            twos=1
        elif s % 3 == 1:
            ones=1
        
    # if max score only needs 3-score problems and we need 1 and 2 score
    # problems (for other scores), then we can replace one of the 3-score problems with the
    # 1 and the 2, which we already need, so we can reduce the result by 
    # one 3-score problem
    if (max_score % 3 == 0) and ones and twos:
        return ones+twos+threes-1
    else:
        return ones+twos+threes

# Test Cases
if __name__ == '__main__':

    #Test 1: 3
    N=5
    S=[1,2,3,4,5]
    print("Test 1 (3):", getMinProblemCount(N,S))
    
    #Test 2: 2
    N=4
    S=[4,3,3,4]
    print("Test 2 (2):", getMinProblemCount(N,S))

    #Test 3: 4
    N=4
    S=[2,4,6,8]
    print("Test 3 (4):", getMinProblemCount(N,S))
    
    #Test 4: 3
    N=1
    S=[8]
    print("Test 4 (3):", getMinProblemCount(N,S))
    