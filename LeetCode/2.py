#!/Users/jnn/Documents/Devel/Challenges/probenv/bin/python3

# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode:
    val,next = 0,None
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2) -> ListNode:
        result = ListNode()
        head = result
        carry = 0
        while l1 or l2:
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            carry = sum // 10
            result.next = ListNode(sum % 10)
            result = result.next
        if carry:
            result.next = ListNode(carry)
        return head.next

if __name__ == '__main__':
    s = Solution()
    # test case 1: [7,0,8]
    one = [9,9,9,9,9,9,9]
    two = [9,9,9,9]

    l1head,l2head = ListNode(),ListNode()
    for i in range(len(one)):
        if i == 0:
            l1 = ListNode(one[i])
            l1head = l1
            continue
        l1.next = ListNode(one[i])
        l1 = l1.next
    for i in range(len(two)):
        if i == 0:
            l2 = ListNode(two[i])
            l2head = l2
            continue
        l2.next = ListNode(two[i])
        l2 = l2.next

    l3=s.addTwoNumbers(l1head,l2head)
    print("Test 1")
    while l3:
        print(l3.val, end=',')
        l3 = l3.next