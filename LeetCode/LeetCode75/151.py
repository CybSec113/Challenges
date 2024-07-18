class Solution:
    def reverseWords(self, s: str) -> str:
        result=""
        words = s.split(' ')

        for a in reversed(words):
            if a=="":
                continue
            else:
                result+=a
                result+=" "

        return result[:-1]


# Test Cases
if __name__ == '__main__':
    sol=Solution()

    # Test 1
    s="a good   example"
    print("Test 1:", sol.reverseWords(s)) 
