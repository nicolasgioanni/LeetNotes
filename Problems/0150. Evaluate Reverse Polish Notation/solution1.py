class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set("+-/*")

        for token in tokens:
            if token in operators:
                if len(stack) < 2:
                    return None

                a, b = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(b + a)
                elif token == "-":
                    stack.append(b - a)
                elif token == "/":
                    stack.append(int(b / a))
                else:
                    stack.append(b * a)
            else:
                stack.append(int(token))
        
        return stack[0]
