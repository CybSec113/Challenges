# A positive integer is considered uniform if all of its digits are equal. 
# For example, 222222 is uniform, while 223223 is not.
# 
# Given two positive integers AA and BB, determine the number of uniform 
# integers between AA and BB, inclusive.
# 
# Please take care to write a solution which runs within the time limit.
# 
# Constraints
#   1 ≤ A ≤ B ≤ 10^12

# Write any import statements here

def getUniformIntegerCountInInterval(A: int, B: int) -> int:
    # Write your code here
    Adigits,Bdigits=0,0
    Afirst,Bfirst=0,0

    # get number of digits for A and B
    for i in range(13):
        if A >= 10**i and A < 10**(i+1):
            Adigits=i+1
        if B >= 10**i and B < 10**(i+1):
            Bdigits=i+1
    
    # get the first digit of A and B to find boundary
    Afirst=A//10**(Adigits-1)
    Bfirst=B//10**(Bdigits-1)

    # all 10**i to 10**(i+1) have exactly 9 uniform integers
    result=9*(Bdigits-Adigits+1)

    # remove overcount beyond boundaries
    if A <= int(str(Afirst)*Adigits):
        result-=Afirst-1
    else:
        result-=Afirst

    if B < int(str(Bfirst)*Bdigits):
        result-=10-Bfirst
    else:
        result-=10-(Bfirst+1)
            
    return result

# Test cases
if __name__ == '__main__':
    # Test 1
    A=75
    B=300
    print("Test 1 (5):", getUniformIntegerCountInInterval(A,B))

    # Test 2
    A=1
    B=9
    print("Test 2 (9):", getUniformIntegerCountInInterval(A,B))

    # Test 3
    A=999999999999
    B=999999999999
    print("Test 3 (1):", getUniformIntegerCountInInterval(A,B))

    # Test 4
    A=10
    B=23
    print("Test 4:", getUniformIntegerCountInInterval(A,B))