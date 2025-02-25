from collections import deque
class Solution:
    def intToRoman(self, num: int) -> str:
        # intRomanMap = {
        #     1: 'I',
        #     5: 'V',
        #     10: 'X',
        #     50: 'L',
        #     100: 'C',
        #     500: 'D',
        #     1000 : 'M',      
        # }
        intRomanMap = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

        res = deque()
        for i in range(4):
            digit = num % 10
            if digit == 4:
                res.appendleft(intRomanMap[i * 2 + 1])
                res.appendleft(intRomanMap[i * 2 ])
            elif digit == 9:
                res.appendleft(intRomanMap[i * 2 + 2])
                res.appendleft(intRomanMap[i * 2 ])
            elif digit == 5:
                res.appendleft(intRomanMap[i * 2 + 1])
            elif digit > 5:
                res.appendleft(intRomanMap[i * 2] * (digit - 5))
                res.appendleft(intRomanMap[i * 2 + 1])
            else:
                res.appendleft(intRomanMap[i * 2] * digit)
            num //= 10
        return ''.join(res)
    
    def intToRoman(self, num: int) -> str:
        roman_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        roman = ""
        for value, symbol in roman_map:
            while num >= value:
                roman += symbol
                num -= value

        return roman
Solution().intToRoman(3999)