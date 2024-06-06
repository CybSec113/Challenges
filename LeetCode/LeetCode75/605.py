class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:

        inArow=0
        plants=0

        if len(flowerbed) == 1:
            if flowerbed[0]==1 and n==1:
                return False
            else: 
                return True

        for i in range(len(flowerbed)):

            if flowerbed[i] == 1:
                inArow=0
                continue

            inArow+=1
            # front edge case
            if i==1 and inArow==2:
                inArow=1
                plants+=1
            
            # back edge case
            elif i==len(flowerbed)-1 and inArow==2:
                plants+=1

            # middle case
            elif inArow==3:
                plants+=1
                inArow=1

            # meets condition
            if plants>=n:
                return True

        return False

# test cases
if __name__ == '__main__':
    s=Solution()

    # Test 0
    a=[1,0,1,0,1,0,1]
    n=1
    print("Test 0:(False)", s.canPlaceFlowers(a,n)) 

    # Test 1
    a=[1,0,1,0,0]
    n=1
    print("Test 1:(True)", s.canPlaceFlowers(a,n)) 

    # Test 2
    a=[1,0,0,0,0,0,1]
    n=2
    print("Test 2:(True)", s.canPlaceFlowers(a,n)) 

    # Test 3
    a=[1,0,0,0,0,1]
    n=2
    print("Test 3:(False)", s.canPlaceFlowers(a,n)) 

    # Test 4
    a=[0]
    n=0
    print("Test 4:(True)", s.canPlaceFlowers(a,n)) 

    # Test 5
    a=[0,0,0,0]
    n=3
    print("Test 5:(False)", s.canPlaceFlowers(a,n)) 
