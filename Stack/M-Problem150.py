class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def plus(a, b):
            return a + b
        def minus(a, b):
            return a - b
        def multiply(a, b):
            return a * b
        def divide(a, b):
            return int(a / b)
        
        operators = {'+': plus, '-': minus, '*': multiply, '/': divide}
        stack = []
        for token in tokens:
            if stack and token in operators.keys():
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(operators.get(token)(num1, num2))
            else:
                stack.append(int(token))
        return stack[0]