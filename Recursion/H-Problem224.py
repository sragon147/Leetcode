class Solution:
    def calculate(self, s: str) -> int:
        sgn = 1
        number = 0
        res = 0
        stack = []
        
        for ch in s:
            if ch.isdigit():
                number = number*10 + int(ch)
            elif ch == '+':
                res  += number*sgn
                sgn = 1
                number = 0
            elif ch == '-':
                res += number*sgn
                sgn = -1
                number = 0
            elif ch == '(':
                stack.append(res)
                stack.append(sgn)
                sgn = 1
                number = 0
                res = 0
            elif ch == ')':
                prev_sgn = stack.pop()
                prev_res = stack.pop()
                res += number*sgn
                res = prev_res + res*prev_sgn
                number = 0

        return res + number*sgn
print(Solution().calculate(" 2-1 + 2 ")) # 2
                