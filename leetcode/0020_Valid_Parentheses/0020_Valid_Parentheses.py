class Solution:
    def isValid(self, s):
        if s is None:
            return True
        stack = collections.deque([])
        c_brackets = {
            ')': '(', 
            '}': '{', 
            ']': '['
        }
        for t in s:
            if t in c_brackets:
                try:
                    current = stack.pop()
                except:
                    return False
                if current != c_brackets[t]:
                        return False
            else:
                stack.append(t)
        if stack:
            return False
        else:
            return True