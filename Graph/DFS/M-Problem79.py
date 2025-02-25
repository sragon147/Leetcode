class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        def dfs(r, c, word):
            if len(word) == 0:
                return True
            
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            
            char = board[r][c]
            if char != word[0]:
                return False
            
            board[r][c] = '#'
            
            up = dfs(r, c - 1, word[1:])
            do = dfs(r, c + 1, word[1:])
            ri = dfs(r + 1, c, word[1:])
            le = dfs(r - 1, c, word[1:])
            
            board[r][c] = char
            
            return up or do or ri or le
        
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, word):
                    return True
        
        return False

    
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])

        if len(word) > row * col:
            return False

        # Count letters in board without using sum(board, [])
        board_count = {}
        for r in range(row):
            for c in range(col):
                board_count[board[r][c]] = board_count.get(board[r][c], 0) + 1

        # Validate board contains enough letters
        word_count = {}
        for char in word:
            word_count[char] = word_count.get(char, 0) + 1

        for char in word_count:
            if board_count.get(char, 0) < word_count[char]:
                return False

        # Optimize search order: Reverse word if the last character appears less than the first
        if board_count.get(word[0], 0) > board_count.get(word[-1], 0):
            word = word[::-1]

        # DFS with in-place marking instead of `seen` set
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= row or c >= col or board[r][c] != word[i]:
                return False

            # Temporarily mark cell as visited
            temp, board[r][c] = board[r][c], '#'

            res = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )

            # Restore cell
            board[r][c] = temp
            return res

        # Start DFS from each matching cell
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False
