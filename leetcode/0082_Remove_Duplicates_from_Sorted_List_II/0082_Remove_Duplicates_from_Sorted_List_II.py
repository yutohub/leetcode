# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head):
        if head is None:
            return None
        dummyhead = ListNode(-101)
        dummyhead.next = head
        ref = dummyhead
        while ref.next != None and ref.next.next != None:
            if ref.next.val == ref.next.next.val:
                search = ref.next.next
                while search.next != None and search.val == search.next.val:
                    search = search.next
                ref.next = search.next
            else:
                ref = ref.next
        return dummyhead.next
        