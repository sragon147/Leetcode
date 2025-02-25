class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        print(path)
        stack = []
        for i in path:
            if not i or i == '.': 
                continue
            if i == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return '/' + '/'.join(stack)
print(Solution().simplifyPath("/a/./b///../../c/"))
