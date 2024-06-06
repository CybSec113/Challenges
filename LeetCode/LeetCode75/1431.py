class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result=list()

        maxCandies=max(candies)
        for i in range(len(candies)):
            result.append(candies[i]+extraCandies >= maxCandies)
        
        return result
    

#Test cases
if __name__ == '__main__':
    s=Solution()

    # test 1
    c=[2,3,5,1,3]
    e=3
    print("Test 1:")
    print("[true, true, true, false, true]")
    print(s.kidsWithCandies(c,e))
    print()

    # test 2
    c=[4,2,1,1,2]
    e=1
    print("Test 2:")
    print("[true, false, false, false, false]")
    print(s.kidsWithCandies(c,e))
    print()

    # test 3
    c=[12,1,12]
    e=10
    print("Test 3:")
    print("[true, false, true]")
    print(s.kidsWithCandies(c,e))
    print()
