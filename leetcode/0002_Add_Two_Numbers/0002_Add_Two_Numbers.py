# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        root = ListNode(0)
        answer = root
        carry = 0
        
        while l1 != None or l2 != None:
            n = 0
            # l1 and l2
            if l1 != None and l2 != None:
                n = (l1.val + l2.val + carry) % 10
                carry = (l1.val + l2.val + carry) // 10
                l1 = l1.next
                l2 = l2.next
            # l1 only
            elif l1 != None:
                n = (l1.val + carry) % 10
                carry = (l1.val + carry) // 10
                l1 = l1.next
            # l2 only
            elif l2 != None:
                n = (l2.val + carry) % 10
                carry = (l2.val + carry) // 10
                l2 = l2.next

            answer.val = n
            
            # does l1 or l2 have next value
            if l1 != None or l2 != None:
                answer.next = ListNode(0)
                answer = answer.next
        
        # if carry remain
        if carry != 0:
            answer.next = ListNode(carry)
        
        return root