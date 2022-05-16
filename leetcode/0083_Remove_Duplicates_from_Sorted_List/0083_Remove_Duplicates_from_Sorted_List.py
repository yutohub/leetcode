# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head):
        if head == None:
            return None
        ref = head
        while ref.next != None:
            if ref.val == ref.next.val:
                ref.next = ref.next.next
            else:
                ref = ref.next
        return head
        