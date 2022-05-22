# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    carry = 0
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        l3 = ListNode()
        l3_begin = l3
        while True:
            sum = 0
            if carry:
                sum += 1
                carry = 0
            sum += l1.val + l2.val
            if sum >= 10:
                sum -= 10
                carry = 1
            l3.val = sum
            if l1.next and l2.next:
                l3.next = ListNode()
                l3 = l3.next
                l2 = l2.next
                l1 = l1.next    
            elif l1.next and not l2.next:
                l3.next = ListNode()
                l3 = l3.next
                l2 = ListNode()
                l1 = l1.next
            elif l2.next and not l1.next:
                l3.next = ListNode()
                l3 = l3.next
                l2 = l2.next
                l1 = ListNode()
            else:
                if carry:
                    l3.next = ListNode()
                    l3 = l3.next
                    l3.val += carry
                    carry = 0
                break
        return l3_begin
            
            
            