class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def devide(sub):
            if not sub: 
                return None
            n = len(sub)
            if n == 1:
                return Node(sub[0][0], True)
            
            mid = n // 2 
            topLeft = devide([row[:mid] for row in sub[:mid]])
            topRight = devide([row[mid:] for row in sub[:mid]])
            bottomLeft = devide([row[:mid] for row in sub[mid:]])
            bottomRight = devide([row[mid:] for row in sub[mid:]])

            return merge(topLeft, topRight, bottomLeft, bottomRight)
        
        def merge(topLeft, topRight, bottomLeft, bottomRight):
            if (topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and
                topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
                return Node(topLeft.val, True)
            
            return Node(None, False, topLeft, topRight, bottomLeft, bottomRight)
        return devide(grid)
    
    def construct(self, grid: List[List[int]]) -> 'Node':
        # NOTE: n == grid.length == grid[i].length
        # And n == 2^x where 0 <= x <= 6
        # e.g. 1x1 up to 64x64
        def solve(r, c, size):
            """
            r: row start
            c: col start
            size: dimension
            """
            startVal = grid[r][c]
            if size == 1:
                return Node(startVal, True)
            allEqual = True
            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != startVal:
                        allEqual = False
                        break
            if allEqual:
                return Node(startVal, True)
            root = Node(1, False)
            topLeft = solve(r, c, size // 2)
            topRight = solve(r, c + size // 2, size // 2)
            bottomLeft = solve(r + size // 2, c, size // 2)
            bottomRight = solve(r + size // 2, c + size // 2, size // 2)
            root.topLeft = topLeft
            root.topRight = topRight
            root.bottomLeft = bottomLeft
            root.bottomRight = bottomRight
            return root
        return solve(0, 0, len(grid))
    
    def construct(self, grid: List[List[int]]) -> 'Node':

        def isAllSame(r, c, size):
            val = grid[r][c]
            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != val:
                        return False
            return True

        def dfs(r, c, size):
            if isAllSame(r, c, size):
                return Node(grid[r][c], True, None, None, None, None)
            
            size = size // 2

            return Node(grid[r][c], 
                        False,
                        dfs(r, c, size),
                        dfs(r, c + size, size),
                        dfs(r + size, c, size),
                        dfs(r + size, c + size, size))

        return dfs(0, 0, len(grid))