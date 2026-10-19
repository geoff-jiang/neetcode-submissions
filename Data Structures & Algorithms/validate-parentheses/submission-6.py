class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        reference = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:
            if c in reference:
                if not stack:
                    return False
                if reference[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        return True if not stack else False
            