class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in "+-/*":
                n1 = stack.pop()
                n2 = stack.pop()
                if t == "+":
                    temp = n2 + n1
                    stack.append(temp)
                elif t == "-":
                    temp = n2 - n1
                    stack.append(temp)
                elif t == "*":
                    temp = n2 * n1
                    stack.append(temp)
                elif t == "/":
                    temp = int(n2/ n1)
                    stack.append(temp)
            else:
                stack.append(int(t))
        return stack.pop()