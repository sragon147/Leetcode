
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {  
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        value = 0
        temp = "M"
        
        for i in s:
            if roman[i] > roman[temp]:
                value -= 2*roman[temp]
                value += roman[i]
            temp = i
        return value