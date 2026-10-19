class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        openSet = set(['(', '[', '{'])
        bracketPairs = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        if len(s) < 2:
            return False

        for c in s:
            if c in openSet:
                q.appendleft(c)
            elif len(q) == 0 or bracketPairs[c] != q[0]:
                return False
            else:
                q.popleft()
        return True if len(q) == 0 else False
        