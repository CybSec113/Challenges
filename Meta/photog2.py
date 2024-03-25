# Write any import statements here
import random
import timeit

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # Write your code here
  result=0
  P = [] 
  A = [] 
  B = [] 

  for i in range(0, len(C)):
    if C[i] == 'P':
      P.append(i)
    elif C[i] == 'A':
      A.append(i)
    elif C[i] == 'B':
      B.append(i)
  #print(P, A, B)

  P_len = len(P)
  A_len = len(A)
  B_len = len(B)

  #PAB
  for p in range(0, P_len):
     for a in range(0, A_len):
       if A[a] >= P[p]:
        for b in range(0, B_len):
          if B[b] >= A[a]:
            #print("a", P[p], A[a], B[b])
            front = abs(A[a]-P[p])
            back = abs(B[b]-A[a])
            if front >= X:
              if front <= Y:
                if back >= X:
                  if back <= Y:
                    result += 1
                    #print("^")

  #BAP
  for b in range(0, B_len):
    for a in range(0, A_len):
      if A[a] >= B[b]:
        for p in range(0, P_len):
          if P[p] >= A[a]:
            #print("b", B[b], A[a], P[p])
            front = abs(A[a]-B[b])
            back = abs(P[p]-A[a])
            if front >= X:
              if front <= Y:
                if back >= X:
                  if back <= Y:
                    result += 1
                    #print("^")

  return result

if __name__ == '__main__':
  photo1='PAB.'
  C=''
  N=2000      # max: 300,000
  C_test = '.PBAAP.B'
  N_test = 7

  for i in range(1, N):
    C += random.choice(photo1)

  start = timeit.default_timer()
  print("result", getArtisticPhotographCount(N, C, 1, 3))
  stop = timeit.default_timer()
  print("time:", stop-start)