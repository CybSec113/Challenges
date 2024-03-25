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
  #print(P)
  #print(A)
  #print(B)

  P_len = len(P)
  A_len = len(A)
  B_len = len(B)

  #PAB
  #print("PAB")
  for p in range(0, P_len):
    for a in range(0, A_len):
      if (A[a] > P[p]):
       if (abs(A[a]-P[p]) >= X) and (abs(A[a]-P[p]) <= Y):
        for b in range(0, B_len):
          if (B[b] > A[a]):
            if (abs(B[b]-A[a]) >= X) and (abs(B[b]-A[a]) <= Y):
              #print("photo", P[p], A[a], B[b])
              result += 1

  #BAP
  #print("BAP")
  for b in range(0, B_len):
    for a in range(0, A_len):
      if A[a] > B[b]:
        if (abs(A[a]-B[b]) >= X) and (abs(A[a]-B[b]) <= Y):
          for p in range(0, P_len):
            if P[p] > A[a]:
              if (abs(P[p]-A[a]) >= X) and (abs(P[p]-A[a]) <= Y):
                #print("photo", B[b], A[a], P[p])
                result += 1

  return result

if __name__ == '__main__':
  photo1='PAB.'
  C=''
  N=15000      # max: 300,000
  C_test1 = 'APABA'
  N_test1=5
  C_test3 = '.PBAAP.B'
  N_test3 = 8

  for i in range(0, N):
    C += random.choice(photo1)
  #print(C)
  #print("len", len(C))

  start = timeit.default_timer()
  print("result", getArtisticPhotographCount(N, C, 1, 3))
  stop = timeit.default_timer()
  print("runtime (secs):", stop-start)