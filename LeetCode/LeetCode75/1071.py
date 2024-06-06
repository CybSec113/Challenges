class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        result=""
        big=""
        small=""
        if len(str1) > len(str2):
            big=str1
            small=str2
        else:
            big=str2
            small=str1

        def amod(s1, s2):
            i=0
            tmp=""

            while i < len(s1):
                tmp+=s2
                if s1==tmp:
                    return 1
                i+=len(s2)
            return 0

        if amod(big, small):
            return small

        tmp=""
        for i in range(len(small)):
            tmp+=small[i]
            if amod(str1, tmp) and amod(str2, tmp):
                result=tmp

        return result
        

# test cases
if __name__ == '__main__':
    s = Solution()

    #test 1
    str1="ABCABC"
    str2="ABC"
    print("Test 1 (ABC):", s.gcdOfStrings(str1, str2))

    #test 2
    str1="ABABAB"
    str2="ABAB"
    print("Test 2 (AB):", s.gcdOfStrings(str1, str2))

    #test 3
    str1="LEET"
    str2="CODE"
    print("Test 3 ():", s.gcdOfStrings(str1, str2))

    #test 4
    str1="ABABABAB"
    str2="ABAB"
    print("Test 4 (ABAB):", s.gcdOfStrings(str1, str2))

    #test 5
    str1="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    str2="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    print("Test 5")
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    print(s.gcdOfStrings(str1, str2))
