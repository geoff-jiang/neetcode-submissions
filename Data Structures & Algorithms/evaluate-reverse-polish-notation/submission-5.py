class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        q = deque() #first in first out! 
        for t in tokens:
            if t == "+":
                q.append(q.pop() + q.pop())
            elif t == "-": 
                a, b = q.pop(), q.pop()
                q.append(b - a)
            elif t == "*":
                q.append(q.pop() * q.pop())
            elif t == "/":
                a, b = q.pop(), q.pop()
                q.append(int(float(b)/ a))
            else:
                q.append(int(t))

        return q[0]

