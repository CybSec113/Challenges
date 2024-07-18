class Solution:
    def reverseVowels(self, s: str) -> str:

        result=list(s)
        vowels="aeiouAEIOU"
        left=0
        right=len(s)-1

        for i in range(len(s)):
            if result[i] in vowels:
                while result[right] not in vowels:
                    right-=1
                if i>=right:
                    break
                c=result[i]
                result[i]=result[right]
                result[right]=c
                right-=1

        return "".join(result)
    

# Test cases
if __name__ == '__main__':
    sol=Solution()

    # test 1
    s="hello"
    print("Test 1:", sol.reverseVowels(s))

    # test 2
    s="leetcode"
    print("Test 2:", sol.reverseVowels(s))
