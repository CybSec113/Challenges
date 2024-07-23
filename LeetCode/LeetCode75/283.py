class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left0=0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                tmp = nums[i]
                nums[i] = nums[left0]
                nums[left0] = tmp
                left0+=1



if __name__ == '__main__':
    s = Solution()

    #Test 1
    nums = [0,1,0,3,12]
    print("Test 1")
    print(nums)
    s.moveZeroes(nums)
    print(nums)

    #Test 2
    nums = [4,2,4,0,0,3,0,5,1,0]
    print("Test 2")
    print(nums)
    s.moveZeroes(nums)
    print(nums)