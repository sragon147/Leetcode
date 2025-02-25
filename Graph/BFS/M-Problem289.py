import collections
from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        ALIVE = 1
        DEAD = 0
        ALIVETOALIVE = 3
        DEADTOALIVE = 2
        rows, cols = len(board), len(board[0])
        def bfs(x: int, y: int):
            count = 0
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
            for direction in directions:
                r, c = x + direction[0], y + direction[1]
                if 0 <= r < rows and 0 <= c < cols and (board[r][c] == ALIVE or board[r][c] == ALIVETOALIVE):
                    count += (board[r][c] & 1)
            return count
        
        for row in range(rows):
            for col in range(cols):
                live_neighbors = bfs(row, col)
                if board[row][col] == ALIVE and (live_neighbors == 2 or live_neighbors == 3):
                        board[row][col] = ALIVETOALIVE
                if board[row][col] == DEAD and live_neighbors == 3:
                        board[row][col] = DEADTOALIVE 
        for row in range(rows):
            for col in range(cols):
                board[row][col] >>= 1
        
    def gameOfLife(self, board: List[List[int]]) -> None:
        def gameOfLifeInfinite(live_cells):
            # Directions to check for each live cell: right, left, down, up, and the 4 diagonals
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
            
            # Step 1: Count the number of live neighbors for each cell
            neighbor_counts = collections.Counter()
            
            # Loop through each live cell in the live_cells set
            for i, j in live_cells:
                # Check all 8 neighboring cells based on the directions
                for di, dj in directions:
                    ni, nj = i + di, j + dj  # Calculate the neighbor's position
                    neighbor_counts[(ni, nj)] += 1  # Increment the count for this neighbor
            
            # Step 2: Determine the new live cells based on the Game of Life rules
            new_live_cells = set()

            # Loop through all counted neighbors
            for cell, count in neighbor_counts.items():
                # Rule 1: A cell becomes live if it has exactly 3 live neighbors
                # Rule 2: A live cell stays alive if it has 2 or 3 live neighbors
                if count == 3 or (count == 2 and cell in live_cells):
                    new_live_cells.add(cell)
            
            # Return the set of new live cells
            return new_live_cells
        live = set()  # Create an empty set to store live cell coordinates

        for i, row in enumerate(board):  # Loop through each row with its index
            for j, cell in enumerate(row):  # Loop through each cell in the row with its index
                if cell == 1:  # If the cell is alive (1)
                    live.add((i, j))  # Add its coordinates (i, j) to the set
        live = gameOfLifeInfinite(live)  # Call the helper function to get the new live cells
        for i, row in enumerate(board):
            for j in range(len(row)):
                if (i, j) in live:
                    row[j] = 1  # Cell is alive
                else:
                    row[j] = 0
Solution().gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])