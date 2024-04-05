# 
# A family of frogs in a pond are traveling towards dry land to hibernate. 
# They hope to do so by hopping across a trail of NN lily pads, numbered from 11 to NN in order.
# 
# There are FF frogs, numbered from 11 to FF. Frog ii is currently perched atop lily pad PiPi​. 
# No two frogs are currently on the same lily pad. Lily pad NN is right next to the shore, 
# and none of the frogs are initially on lily pad NN.
# 
# Each second, one frog may hop along the trail towards lily pad NN. When a frog hops, it moves to 
# the nearest lily pad after its current lily pad which is not currently occupied by another frog 
# (hopping over any other frogs on intermediate lily pads along the way). If this causes it to reach 
# lily pad NN, it will immediately exit onto the shore. Multiple frogs may not simultaneously hop 
# during the same second.
# 
# Assuming the frogs work together optimally when deciding which frog should hop during each second, 
# determine the minimum number of seconds required for all FF of them to reach the shore.
# 
# Constraints
#    2 ≤ N ≤10^12
#    1 ≤ F ≤ 500,000
#    1 ≤ Pi ≤ N−1
# 
from typing import List
# Write any import statements here

def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
    # Write your code here
    # If there are N pads and F frogs, best case outcome is F seconds.
    # So, let's always move the furthest frog to the next empty pad.
    # With F frogs, if F-1 are bunched up in front of N, then the last
    # frog must hop N-F-[last frog index] to join the bunch
    # But this is also true if the F-1 frogs aren't bunched up;
    # the last frog will always need to jump N-F-[last frog index] to join the bunch
    # So solution is simply N-[last frog index] which is min(P)
    return N-min(P)

# Test cases
if __name__ == '__main__':
    # Test 1
    N=3
    F=1
    P=[1]
    print("Result 1 (2):", getSecondsRequired(N,F,P))

    # Test 2
    N=6
    F=3
    P=[5,2,4]
    print("Result 2 (4):", getSecondsRequired(N,F,P))
