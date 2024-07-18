class Solution:
    def compress(self, chars: list[str]) -> int:
        for x in chars:
            for y in chars[1:]:
                count=0
                while y != x:
                    count+=1
                    continue
                print(count)
        return len(chars)


if __name__ == '__main__':
    s = Solution()

    #Test 1:
    chars = ["a","a","b","b","c","c","c"]
    print("Test 1(a2b2c3):", s.compress(chars))
