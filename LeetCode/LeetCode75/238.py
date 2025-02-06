class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        pre = [0] * n
        suff = [0] * n
        result = [0] * n

        pre[0] = 1
        for i in range(1, n):
            pre[i] = pre[i-1] * nums[i-1]
        print(pre)

        suff[n-1] = 1
        for i in range(n-2,-1,-1):
            suff[i] = suff[i+1] * nums[i+1]
        print(suff)

        for i in range(n):
            result[i] = pre[i] * suff[i]
        print(result)

        return result
    

# Test Cases
if __name__ == '__main__':
    s=Solution()

    # Test 1
    nums=[2,3,4,5,6,7];
    print("Test 1:", s.productExceptSelf(nums))
