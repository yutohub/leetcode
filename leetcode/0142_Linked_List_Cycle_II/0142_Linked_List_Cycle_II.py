# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):       
        try:
            fast = head.next.next
            slow = head.next
            while fast != slow:
                fast = fast.next.next
                slow = slow.next
            else:
                slow = head # Restart
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                else:
                    return slow
        except:
            return None
