#Given an array of integers nums which is sorted in ascending order, 
#and an integer target, write a function to search target in nums. 
#If target exists, then return its index. Otherwise, return -1.
#
#You must write an algorithm with O(log n) runtime complexity.
#

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1

        while left <= right:
            mid=left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left=mid+1
            elif target < nums[mid]:
                right=mid-1
        
        return -1
        

# Test Cases
if __name__ == '__main__':
    s = Solution()

    # Test 1: 4
    N=[-1,0,3,5,9,12]
    T=9
    print("Test 1 (4):", s.search(N,T))

    # Test 2: -1
    N=[-1,0,3,5,9,12]
    T=2
    print("Test 2 (-1):", s.search(N,T))

    # Test 3:0
    N=[5]
    T=5
    print("Test 3 (0):", s.search(N,T))