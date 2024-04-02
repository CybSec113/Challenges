def minimumBribes(q):

    result=0
    for i in range(0,len(q)):
        if q[i]-(i+1) > 2:
            print("Too chaotic")
            return

        for j in range(max(0, q[i]-2), i):
            if q[j]>q[i]:
                result+=1
    print(result)



if __name__ == '__main__':
    q=[1,2,3,5,4,6,7,8]
    print("===> Test 1 (1)")
    minimumBribes(q)

    q=[4,1,2,3]
    print("===> Test 2 (Too chaotic)")
    minimumBribes(q)

    q=[5,1,2,3,7,8,6,4]
    print("===> Test 3 (Too chaotic)")
    minimumBribes(q)

    q=[1,2,5,3,7,8,6,4]
    print("===> Test 4 (7)")
    minimumBribes(q)