class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=""
        w1=len(word1)
        w2=len(word2)
        i=0
        while i < min(w1,w2):
            result+=word1[i]
            result+=word2[i]
            i+=1
        
        if w1 > w2:
            result+=word1[w2:]
        elif w1 < w2:
            result+=word2[w1:]

        return result

if __name__ == '__main__':
    s=Solution()

    # test 1
    word1="abc"
    word2="pqr"
    print("Test 1:", s.mergeAlternately(word1, word2))

    # test 2
    word1="ab"
    word2="pqrs"
    print("Test 2:", s.mergeAlternately(word1, word2))