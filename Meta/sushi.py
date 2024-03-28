from typing import List
# Write any import statements here
import timeit

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    # Write your code here
    result=0
    hist=[]
    for n in range(0, N):
        if D[n] not in hist:
            result+=1
            hist.append(D[n])
            if len(hist)>K:
                hist.remove(hist[0])

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

    start = timeit.default_timer()
    print("result:", getMaximumEatenDishCount(N3,D3,K3))
    stop = timeit.default_timer()
    print("runtime (secs):", stop-start)