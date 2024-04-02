# There is an integer array nums sorted in ascending order (with distinct values).
# 
# Prior to being passed to your function, nums is possibly rotated at an unknown 
# pivot index k (1 <= k < nums.length) such that the resulting array is 
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# 
# Given the array nums after the possible rotation and an integer target, return the index 
# of target if it is in nums, or -1 if it is not in nums.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# Constraints:
# 
#     1 <= nums.length <= 5000
#     -10^4 <= nums[i] <= 10^4
#     All values of nums are unique.
#     nums is an ascending array that is possibly rotated.
#     -10^4 <= target <= 10^4
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # edge case
        if len(nums) <= 5:
            for i in range(len(nums)):
                if target == nums[i]:
                    return i
            return -1

        # List is rotated
        left=0
        right=len(nums)-1
        numsorted=nums
        if nums[0] > nums[len(nums)-1]:
            while left<=right:
                mid=left+(right-left)//2
                if nums[left] < nums[len(nums)-1]:
                    numsorted=nums[left:]+nums[0:left]
                    break
                if nums[left] < nums[mid]:
                    left=mid+1
                elif nums[left] > nums[mid]:
                    right=mid-1
        print(numsorted)

        # now find target
        pivot=left
        left=0
        right=len(numsorted)-1
        while left<=right:
            mid=left+(right-left)//2
            if target == numsorted[mid]:
                return (mid+pivot)%len(nums)
            elif target > numsorted[mid]:
                left=mid+1
            elif target < numsorted[mid]:
                right=mid-1

        return -1

# Test Cases
if __name__ == '__main__':
    s = Solution()
    
    nums=[3,4,5,6,1,2]
    target=2
    print("Test 0 (6):",s.search(nums, target))

    nums=[4,5,6,7,0,1,2]
    target=5
    print("Test 1 (1):",s.search(nums, target))

    nums=[4,5,6,7,0,1,2]
    target=3
    print("Test 2 (-1):",s.search(nums, target))

    nums=[1]
    target=1
    print("Test 3 (0):",s.search(nums, target))

    nums=[3,1]
    target=1
    print("Test 4 (1):",s.search(nums, target))


    nums=[3,5,1]
    target=0
    print("Test 5 (-1):",s.search(nums, target))