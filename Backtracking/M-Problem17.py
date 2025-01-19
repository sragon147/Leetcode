from typing import List
from collections import deque

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        dict = {
            '2':['a', 'b', 'c'],
            '3':['d', 'e', 'f'],
            '4':['g', 'h', 'i'],
            '5':['j', 'k', 'l'],
            '6':['m', 'n', 'o'],
            '7':['p', 'q', 'r', 's'],
            '8':['t', 'u', 'v'],
            '9':['w', 'x', 'y', 'z'],
        }
        stack = deque()
        stack.append('')
        # for i in range(len(digits)):
        #     while len(stack[-1]) < i+1:
        #         s = stack.pop()
        #         for letter in dict[digits[i]]:              
        #             stack.appendleft(s + letter)
        while len(stack[0]) < len(digits):
            s = stack.popleft()
            for letter in dict[digits[len(s)]]:
                stack.append(s + letter )

        return list(stack)
    

Solution().letterCombinations('23')
        

