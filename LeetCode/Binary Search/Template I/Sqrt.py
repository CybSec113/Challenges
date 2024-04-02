# Given a non-negative integer x, return the square root of x 
# rounded down to the nearest integer. The returned integer should 
# be non-negative as well.
#
# You must not use any built-in exponent function or operator.
#
#     For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
#

# Constraints: 0 <= x <= 2^31 - 1

class Solution:
    def mySqrt(self, x: int) -> int:
        result=0
        left=0
        right=46341  # ~ sqrt(2^31)

        while left <= right:
            mid=left + (right-left)//2
            if mid*mid <= x and (mid+1)*(mid+1) > x:
                return mid
            if mid*mid < x:
                left=mid+1
            else: right=mid-1

        return result



# Test Cases
if __name__ == '__main__':
    s = Solution()

    print("Test 1 (2):", s.mySqrt(4))
    print("Test 2 (2):", s.mySqrt(8))