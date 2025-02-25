class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        board = [[0] * n for _ in range(n)]

        def is_safe(r, c):
            for i in range(r):
                if board[i][c] == 1:
                    return False
                if c - (r - i) >= 0 and board[i][c - (r - i)] == 1:
                    return False
                if c + (r - i) < n and board[i][c + (r - i)] == 1:
                    return False
            return True

        def backtrack(row):
            nonlocal res
            if row == n:
                res += 1
                return

            for col in range(n):
                if is_safe(row, col):
                    board[row][col] = 1
                    backtrack(row + 1)
                    board[row][col] = 0

        backtrack(0)
        return res

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        cols = [False]*n
        r_diag = [False]*2*n
        l_diag = [False]*2*n
        count = 0

        def backtrack(row):
            nonlocal count
            if row == n:
                count += 1
                return
            
            for col in range(n):
                r_d = row+col
                l_d = row-col

                if cols[col] or r_diag[r_d] or l_diag[l_d]:
                    continue
                
                cols[col] = r_diag[r_d] = l_diag[l_d] = True
                backtrack(row+1)
                cols[col] = r_diag[r_d] = l_diag[l_d] = False

        ans = backtrack(0, 0)
        return ans