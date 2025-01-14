class Solution:
    def isValid(self, s: str) -> bool:
        matcher = {"(": ")", "{": "}", "[":"]"}
        stack = []
        for c in s:
            if c in matcher:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                left = stack.pop()
                if matcher[left] != c:
                    return False
        return len(stack) == 0