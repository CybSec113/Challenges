class Solution:
    def compress(self, chars: list[str]) -> int:
        count=1 #keep track of number of repeated chars
        front=0 #keep track of current char
        index=1 #keep track of next char, since we are deleting repeated chars.

        # add multi-digit ints as individual chars
        def int2chars(x,index):
            strx=str(x)
            for c in strx:
                if index<len(chars):
                    chars.insert(index,c)
                    index+=1
                else:
                    chars.append(c)
                    index+=1

        # base case
        if len(chars)==1:
            return len(chars)

        while index < len(chars):
            if chars[front] == chars[index]:
                count+=1
                del chars[index]
            else:
                if count>1:
                    int2chars(count,index)
                    front+=1+len(str(count))
                    index+=1+len(str(count))
                if count==1:
                    front+=len(str(count))
                    index+=len(str(count))
                count=1
        
        if count>1:
            int2chars(count,index)

        return len(chars)


if __name__ == '__main__':
    s = Solution()

    #Test 1:
    chars = ["a","a","b","b","c","c","c"]
    ret=s.compress(chars)
    print("Test 1(a2b2c3):",ret,chars)

    #Test 2:
    chars = ["a"]
    ret=s.compress(chars)
    print("Test 2(a):",ret,chars)

    #Test 3:
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b","c"]
    ret=s.compress(chars)
    print("Test 3(a,b12):",ret,chars)

    #Test 4:
    chars = ["a","a","a","b","b","a","a"]
    ret=s.compress(chars)
    print("Test 4(a3b2a2):",ret,chars)
