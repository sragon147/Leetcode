class Solution:
    def decodeString(self, s: str) -> str:
        res = []
        i = 0
        while i < len(s):
            if s[i] == ']':
                char = ''
                while res and res[-1] != '[':
                    char = res.pop() + char
                print(char)
                res.pop()
                times = ''
                while res and res[-1] != '[' and res[-1].isdigit():
                    times = res.pop() + times
                print(times)
                res.append(char * int(times))
                print(res)
            else:
                res.append(s[i])
            i += 1
        return ''.join(res)

Solution().decodeString("3[a]2[bc]")