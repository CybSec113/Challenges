# Write any import statements here
import numpy
import random
import timeit

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # Write your code here
  photo1='PAB'
  photo2='BAP'
  substr=[0,0,0]
  result = 0

  #This 2D array keeps track of 'PAB' and 'BAP' sequences in C
  A = numpy.zeros((len(photo1),len(C)), dtype=int)

  for i in range(0, len(photo1)):
    for j in range(0, len(C)):
      if photo1[i] == C[j]:
        A[i][j] = 1
  #print(A)

  #This loop counts 'PAB' sequences in A and determines if they are 'artistic'
  #print("PAB")
  for j in range(0, len(A[0])):
    if A[0][j] == 1:
      substr[0] = j
      #print("a", 0, j, substr)
      for jj in range(j+1, len(A[1])):
        if A[1][jj] == 1:
          substr[1] = jj
          #print("b", 1, jj, substr)
          for jjj in range(jj+1, len(A[2])):
            if A[2][jjj] == 1:
              substr[2] = jjj
              #print("c", 2, jjj, substr)
              if (substr[1] - substr[0]) >= X:
                if (substr[1] - substr[0]) <= Y:
                  if (substr[2] - substr[1]) >= X:
                    if (substr[2] - substr[1]) <= Y:
                      result += 1
              substr[2] = 0
          substr[1] = 0
      substr[0] = 0

  #This loop counts 'BAP' sequences in A and determines if they are 'artistic'
  #print("BAP")
  for j in range(0, len(A[2])):
    if A[2][j] == 1:
      substr[0] = j
      #print("a", 2, j, substr)
      for jj in range(j+1, len(A[1])):
        if A[1][jj] == 1:
          substr[1] = jj
          #print("b", 1, jj, substr)
          for jjj in range(jj+1, len(A[0])):
            if A[0][jjj] == 1:
              substr[2] = jjj
              #print("c", 0, jjj, substr)
              if (substr[1] - substr[0]) >= X:
                if (substr[1] - substr[0]) <= Y:
                  if (substr[2] - substr[1]) >= X:
                    if (substr[2] - substr[1]) <= Y:
                      result += 1
              substr[2] = 0
          substr[1] = 0
      substr[0] = 0

  return result

if __name__ == '__main__':
  photo1='PAB.'
  C=''
  N=1000
  C_test = '.PBAAP.B'
  N_test = 7

  for i in range(1, N):
    C += random.choice(photo1)

  start = timeit.default_timer()
  print("result", getArtisticPhotographCount(N, C, 1, 3))
  stop = timeit.default_timer()
  print("time:", stop-start)