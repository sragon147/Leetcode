from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        bfs = [1]
        rows = len(board)
        cols = len(board[0])
        need = {1:0}
        for start in bfs:
            for next in range(start + 1, start + 7):
                row = (next - 1) // rows
                col = (next - 1) % cols
                
                if row % 2 != 0:
                    col = cols - col - 1 
                row = rows - row - 1

                if board[row][col] != -1:
                    next = board[row][col]

                if next == rows * cols:
                    return need[start] + 1
                
                if next not in need:
                    need[next] = need[start] + 1
                    bfs.append(next)
        return -1
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        bfs = deque([(1, 0)])
        rows = len(board)
        cols = len(board[0])
        visited = set([1])
        while bfs:
            start, move = bfs.popleft()
            for next in range(start + 1, start + 7):
                row = (next - 1) // cols
                col = (next - 1) % cols
                
                if row % 2 != 0:
                    col = cols - col - 1 
                row = rows - row - 1

                if board[row][col] != -1:
                    next = board[row][col]

                if next == rows * cols:
                    return move + 1
                
                if next not in visited:
                    visited.add(next)
                    bfs.append((next, move + 1))
        return -1

Solution().snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]])