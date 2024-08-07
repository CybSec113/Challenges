class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # base cases
        if len(t) < len(s):
            return False
        if s == t:
            return True

        # general cases
        tindex=0
        for i in range(len(s)):
            for j in range (tindex,len(t)):
                if s[i] == t[j]:
                    tindex=j
                    break

        return True
        

if __name__ == '__main__':
    sol = Solution()

    # Test 1
    s='abc'
    t='ahbgdc'
    print("Test 1(T):",sol.isSubsequence(s,t))

    # Test 2
    s='axc'
    t='ahbgdc'
    print("Test 2(F):",sol.isSubsequence(s,t))
