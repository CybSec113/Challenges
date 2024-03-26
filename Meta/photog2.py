# Write any import statements here
import random
import timeit

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # Write your code here
  result=0

  for a in range(0, len(C)):
    if C[a] == 'A':
      p=max(0, a-1)
      while p>=0:
        if abs(a-p)>Y:
          break
        if abs(a-p)<X:
          p-=1
          continue
        if C[p] == 'P':
          b=min(a+1, len(C))
          while b<len(C):
            if abs(b-a)>Y:
              break
            if abs(b-a)<X:
              b+=1
              continue
            if (C[b]=='B'):
              print("photo:", p, a, b)
              result+=1
            b+=1
        p-=1
              
      b=max(0, a-1)
      while b>=0:
        if abs(a-b)>Y:
          break
        if abs(a-b)<X:
          b-=1
          continue
        if C[b] == 'B':
          p=min(a+1, len(C))
          while p<len(C):
            if abs(p-a)>Y:
              break
            if abs(p-a)<X:
              p+=1
              continue
            if (C[p]=='P'):
              print("photo:", b, a, p)
              result+=1
            p+=1
        b-=1

  return result

if __name__ == '__main__':
  photo1='PAB.'
  C=''
  N=100      # max: 300,000
  C_test1 = '.PBAAP.B'
  N_test1 = 8
  C_test2 = 'BBBPPP..A.PAB.PAAABBA.PAB..PPPPAPABBB.BPAAPP.PAAAAA..B.BAB.ABA..PPBBAB.P.P.PPB.PABPP..BAPP..B.BP.B..'
  N_test2 = 100
  #          01234567890123456789
  C_test3 = '.B.BA..P..A..B......'
  N_test3 = 20

  #for i in range(0, N):
  #  C += random.choice(photo1)
  #print(C)
  #print("len", len(C))

  start = timeit.default_timer()
  print("result", getArtisticPhotographCount(N_test3, C_test3, 2, 3))
  stop = timeit.default_timer()
  print("runtime (secs):", stop-start)