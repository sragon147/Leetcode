class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = ""
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                print(i, a[2])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                print(j, b[j])
                j -= 1
            s = str(carry % 2) + s
            print(s, carry // 2, "\n")
            carry //= 2
        return s
    
Solution().addBinary("1101", "11") # "100"