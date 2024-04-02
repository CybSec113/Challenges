# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
import random

def guess(N:int) -> int:
    number=13
    if number > N:
        return 1
    elif number < N:
        return -1
    else: return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        left=0
        right=n
        while left <= right:
            mid=left+(right-left)//2
            if guess(mid) == 0:
                return mid
            elif guess(mid) < 0:
                right=mid-1
            elif guess(mid) > 0:
                left=mid+1
        return -1
        

# Test Cases
if __name__ == '__main__':
    s = Solution()

    print("Test 1:", s.guessNumber(15))