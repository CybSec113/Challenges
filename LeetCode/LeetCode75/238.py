class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        zeroes=nums.count(0)
        if zeroes > 1:
            return [0]*len(nums)

        result=list()
        prod=1
        for i in nums:
            if i != 0:
                prod *= i

        if zeroes:
            for i in nums:
                if i==0:
                    result.append(prod)
                else:
                    result.append(0)
        else:
            for i in nums:
                result.append(prod//i)

        return result
    

# Test Cases
if __name__ == '__main__':
    s=Solution()

    # Test 1
    nums=[1,0,4,5]
    print("Test 1:", s.productExceptSelf(nums))
