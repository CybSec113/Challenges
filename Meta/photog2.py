# Write any import statements here
import random
import timeit

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # Write your code here
  result=0
  left_beg,left_end,right_beg,right_end=0,0,0,0

  for a in range(0, N):
    if C[a] == 'A':
      if (a-X < 0):
        continue
      if (a+X > N-1):
        break
      left_beg = max(0, a-Y)
      left_end = a-X
      right_beg = a+X
      right_end = min(N-1, a+Y)
      Pleft=C.count('P',left_beg, left_end+1)
      Bleft=C.count('B',left_beg, left_end+1)
      Pright=C.count('P',right_beg, right_end+1)
      Bright=C.count('B',right_beg, right_end+1)
      result += (Pleft*Bright) + (Bleft*Pright)

  return result

if __name__ == '__main__':
  photo1='PAB.'
  C=''
  N=300000      # max: 300,000
  #   01234567
  C1='.PBAAP.B'
  N1=8

  for i in range(0, N):
    C += random.choice(photo1)
  #print(C)
  #print("len", len(C))

  beg = timeit.default_timer()
  print("result", getArtisticPhotographCount(N,C,1,150000))
  #print("result", getArtisticPhotographCount(N1,C1,1,3))
  #cProfile.run('getArtisticPhotographCount(8,\'.PBAAP.B\',1,3)')
  stop = timeit.default_timer()
  print("runtime (secs):", stop-beg)