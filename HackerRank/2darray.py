def hourglassSum(arr):
    # Write your code here

    result=0
    hourglass=[]
    for i in range(4):
        for j in range(4):
            # top
            result+=arr[i][j]
            result+=arr[i][j+1]
            result+=arr[i][j+2]
            # middle
            result+=arr[i+1][j+1]
            # bottom
            result+=arr[i+2][j]
            result+=arr[i+2][j+1]
            result+=arr[i+2][j+2]
            hourglass.append(result)
            result=0

    return max(hourglass)


# Test cases
if __name__ == '__main__':
    a=[[1,1,1,0,0,0],\
       [0,1,0,0,0,0],\
       [1,1,1,0,0,0],\
       [0,0,2,4,4,0],\
       [0,0,0,2,0,0],\
       [0,0,1,2,4,0]]
    print("Test 1 (19):", hourglassSum(a)) 