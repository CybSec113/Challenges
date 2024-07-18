class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        small,big = 2**31, 2**31
        for i in nums:
            if i <= small:
                small = i
            elif i <= big:
                big = i
            else:
                return True
        return False
        


if __name__ == '__main__':
    s = Solution()

    # Test 1
    nums=[1,2,3,4,5]
    print("Test 1(T):", s.increasingTriplet(nums)==True)

    # Test 2
    nums=[5,4,3,2,1]
    print("Test 2(F):", s.increasingTriplet(nums)==False)

    # Test 3
    nums=[2,1,5,0,4,6]
    print("Test 3(T):", s.increasingTriplet(nums)==True)

    # Test 4
    nums=[1,1,1,1,1,1,1,1,1]
    print("Test 4(F):", s.increasingTriplet(nums)==False)

    # Test 5
    nums=[1,2,1,3]
    print("Test 5(T):", s.increasingTriplet(nums)==True)

    # Test 6
    nums=[2,4,-2,-3]
    print("Test 6(F):", s.increasingTriplet(nums)==False)

    # Test 7
    nums=[6,7,1,2]
    print("Test 7(F):", s.increasingTriplet(nums)==False)

    # Test 8
    nums=[1,5,0,4,1,3]
    print("Test 8(T):", s.increasingTriplet(nums)==True)
