from typing import List
# Write any import statements here
import random
import timeit

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    # Write your code here
    result=0
    hist=set()
    oldest=D[0]

    for n in range(0, N):
        if D[n] in hist:
            continue
        result+=1
        hist.add(D[n])
        if len(hist)>K:
            for i in hist:
                oldest = i
                break
            hist.remove(oldest)

    return result


if __name__ == '__main__':
    N1=6
    D1=[1,2,3,3,2,1]
    K1=1

    N2=6
    D2=[1,2,3,3,2,1]
    K2=2

    N3=7
    D3=[1,2,1,2,1,2,1]
    K3=2

    #N4=500000    #max 500,000
    #D4=[]
    #K4=N4
    #for i in range(0,N4):
        #D4.append(random.choice(range(1,N4+1)))

    start = timeit.default_timer()
    print("result:", getMaximumEatenDishCount(N3,D3,K3))
    stop = timeit.default_timer()
    print("runtime (secs):", stop-start)