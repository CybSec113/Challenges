# Write any import statements here

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # Write your code here
    result=0
    actors=[]
    Pcount,Bcount=0,0
    Pcount_before_index=[0]
    Bcount_before_index=[0]

    #find index of all As and keep a running count of Ps and Bs at index i
    for i in range(N):
        if C[i]=='A':
            actors.append(i)
        elif C[i]=='P':
            Pcount+=1
        elif C[i]=='B':
            Bcount+=1
        Pcount_before_index.append(Pcount)
        Bcount_before_index.append(Bcount)
    
    #for each index where there is an A, find Ps and Bs before and after
    #for each A, result += num_Ps_before * num_Bs_after + num_Bs_before * num_Ps_after
    for a in actors:
        #left window
        left_beg=max(0, a-Y)
        left_end=max(0, a-X+1)
        #right window
        right_beg=min(N, a+X)
        right_end=min(N, a+Y+1)

        #PAB
        result+=(Pcount_before_index[left_end]-Pcount_before_index[left_beg])* \
            (Bcount_before_index[right_end]-Bcount_before_index[right_beg])
        #BAP
        result+=(Bcount_before_index[left_end]-Bcount_before_index[left_beg])* \
            (Pcount_before_index[right_end]-Pcount_before_index[right_beg])

    return result

# Test Cases
if __name__ == '__main__':

    # Test Case 1
    C='APABA'
    N=5
    X=1
    Y=3
    print("Test 1", getArtisticPhotographCount(N,C,X,Y))

    # Test Case 2
    C='APABA'
    N=5
    X=2
    Y=3
    print("Test 2", getArtisticPhotographCount(N,C,X,Y))

    # Test Case 3
    C='.PBAAP.B'
    N=8
    X=1
    Y=3
    print("Test 3", getArtisticPhotographCount(N,C,X,Y))
