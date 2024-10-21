def generateParenthesis(n):
    def dfs(left, right, s):
        if len(s) == n * 2:
            res.append(s)
            return  
        if left < n:
            dfs(left + 1, right, s + '(')
        if right < left:
            dfs(left, right + 1, s + ')')
        print(s)
    res = []
    dfs(0, 0, '')
    return res

def main():
    nums = 2

    generateParenthesis(nums)

if __name__ == '__main__':
    main()  # Call the main function