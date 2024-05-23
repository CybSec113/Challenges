# You are given an integer array cards where cards[i] represents the value of the ith card. 
# A pair of cards are matching if the cards have the same value.
# 
# Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. 
# If it is impossible to have matching cards, return -1.
# 
# Constraints:
# 
#     1 <= cards.length <= 10**5
#     0 <= cards[i] <= 10**6
# 

class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        result=10**5 + 1
        pairs=dict()
        count=0

        # dict where cards[x] is key and x is value
        for x in range(len(cards)):
            if cards[x] not in pairs:
                pairs[cards[x]] = x
            else:
                # to look for min, compare current index, x, with prior index, x, stored in cards[x]
                if (x - pairs[cards[x]]) < result:
                    result = x - pairs[cards[x]] + 1
                pairs[cards[x]] = x

        # result initialized to max constraint + 1
        if result == 10**5 + 1:
            result = -1

        return result
        

# test cases
if __name__ == '__main__':

    s = Solution()

    # test 1
    c=[3,4,2,3,4,7]
    print("Test 1(4):", s.minimumCardPickup(c))

    # test 2
    c=[95,11,8,65,5,86,30,27,30,73,15,91,30,7,37,26,55,76,60,43,36,85,47,96,6]
    print("Test 2(3):", s.minimumCardPickup(c))

    # test 3
    c=[77,10,11,51,69,83,33,94,0,42,86,41,65,40,72,8,53,31,43,22,9,94,45,80,40,0,84,34,76,28,7,79,80,93,20,82,36,74,82,89,74,77,27,54,44,93,98,44,39,74,36,9,22,57,70,98,19,68,33,68,49,86,20,50,43]
    print("Test 3(3):", s.minimumCardPickup(c))
