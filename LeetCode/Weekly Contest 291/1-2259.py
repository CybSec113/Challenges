# You are given a string number representing a positive integer and a character digit.

# Return the resulting string after removing exactly one occurrence of digit from number 
# such that the value of the resulting string in decimal form is maximized. 
# The test cases are generated such that digit occurs at least once in number.
# Constraints:
# 
#     2 <= number.length <= 100
#     number consists of digits from '1' to '9'.
#     digit is a digit from '1' to '9'.
#     digit occurs at least once in number.


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        count = number.count(digit)
        # base case
        if count == 1:
            return number[:number.find(digit)] + number[number.find(digit)+1:]
        index=0
        # if digit at index, i, is less than index, i+1, remove that digit and return!
        # there are 3 cases: 
        # 1 - digit[i] < digit[i+1]: remove digit[i]
        # 2 - digit[i] = digit[i+1]: do nothing, continue
        # 3 - digit[i], where i = len(number): more digit[i]
        for i in range(0, count+1):
            index = number.find(digit, index)
            if index == len(number)-1:
                return number[:-1]
            if int(digit) < int(number[index+1]):
                return number[:number.find(digit, index)] + number[number.find(digit, index)+1:]
            if int(digit) == int(number[index+1]):
                index += 1
                continue
            index += 1

        return number[:number.rfind(digit)] + number[number.rfind(digit)+1:]

# test cases
if __name__ == '__main__':

    s=Solution()

    # Test 1
    #n="123"
    #d="3"
    #print("Test 1(12):", s.removeDigit(n,d))

    # Test 2
    #n="1231"
    #d="1"
    #print("Test 2(231):", s.removeDigit(n,d))

    # Test 3
    #n="551"
    #d="5"
    #print("Test 3(51):", s.removeDigit(n,d))

    # Test 4
    #n="133235"
    #d="3"
    #print("Test 4(13325):", s.removeDigit(n,d))

    # Test 5
    #n="7795478535679443616467964135298543163376223791274561861738666981419251859535331546947347395531332878"
    #d="5"
    #print("Test 5:")
    #print("779547853679443616467964135298543163376223791274561861738666981419251859535331546947347395531332878")
    #print(s.removeDigit(n,d))

    # Test 5
    #n="541596"
    #d="5"
    #print("Test 5(54196):", s.removeDigit(n,d))

    # Test 6
    n="1148124977752374816246685216173467327242"
    d="1"
    print("Test 6:")
    print("148124977752374816246685216173467327242")
    print(s.removeDigit(n,d))
