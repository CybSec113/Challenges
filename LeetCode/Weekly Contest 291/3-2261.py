class Solution:
    def countDistinct(self, nums: list[int], k: int, p: int) -> int:
        ans=list()
        tmp=list()
        for i in range(len(nums)):
            divs=0  # number of divisors found
            tmp.clear()

            for j in range(i, len(nums)):
                if not nums[j]%p:
                    if divs==k:
                        break
                    else:
                        divs+=1

                tmp.append(nums[j])
                ans.append(tmp.copy())

        return len(set(tuple(i) for i in ans))
        

if __name__ == '__main__':
    s = Solution()

    # test 1
    nums=[2,3,3,2,2]
    k=2
    p=2
    print("Test 1(11):", s.countDistinct(nums, k, p))

    # test 2
    nums=[1,2,3,4]
    k=4
    p=1
    print("Test 2(10):", s.countDistinct(nums, k, p))

    # test 3
    nums=[13,4,14,13,15,4,8,13,4,12]
    k=5
    p=14
    print("Test 3(50):", s.countDistinct(nums, k, p))

    # test 4
    nums=[10,2,17,7,20]
    k=1
    p=10
    print("Test 4(14):", s.countDistinct(nums, k, p))

    # test 5
    nums=[143,154,89,76,5,43,186,127,99,107,57,68,48,94,133,194,42,15,196,189,128,10,54,166,183,168,146,36,168,150,159,59,141,10,105,164,104,104,161,190,142,42,3,52,53,31,26,41,78,62,147,172,189,56,94,51,161,169,16,53,9,48,15,10,118,57,19,42,122,99,117,194,139,140,91,193,198,39,127,122,70,8,45,142,7,41,78,43,92,60,101,84,193,80,193,120,122,89,2,42,183,177,9,169,196,21,143,78,196,13,152,76,70,157,182,175,28,142,66,14,152,162,44,69,197,83,131,93,89,196,120,42,53,186,185,14,140,98,104,62,38,61,87,147,19,66,69,39,91,72,95,182,107,153,24,109,18,36,157,147]
    k=123
    p=119
    print("Test 5():", s.countDistinct(nums, k, p))
