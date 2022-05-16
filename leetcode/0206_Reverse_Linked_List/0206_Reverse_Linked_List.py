class Solution:
    def reverseList(self, head):
        if head == None:
            return None
        stack = collections.deque([])
        while head != None:
            stack.append(head.val)
            head = head.next
        ans = ListNode(0)
        ref = ans
        while stack:
            n = stack.pop()
            ref.next = ListNode(n)
            ref = ref.next
        return ans.next