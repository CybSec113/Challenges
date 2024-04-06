from typing import List
# Write any import statements here
import math

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  # Write your code here
  
  S.sort()
  
  result = 0
  # front and back edge case
  result = max(math.ceil((S[0] - K - 1) / (K + 1)), 0)
  print("a", result)
  result += max(math.ceil((N - S[M-1] - K) / (K + 1)), 0)
  print("b", result)
  
  if len(S) == 1:
    return result;

  # middle cases
  for i in range(0, M-1):
    result += math.ceil(((S[i+1]-K-1) - (S[i]+K+1) + 1) / (K+1))
    print("c", result)
  
  return result

if __name__ == '__main__':
  print("result", getMaxAdditionalDinersCount(15, 3, 1, [6]))