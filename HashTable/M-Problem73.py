class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        index_of_0 = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    index_of_0.append((i, j))
        for index in index_of_0:
            for i in range(len(matrix)):
                matrix[i][index[1]] = 0
            for j in range(len(matrix[0])):
                matrix[index[0]][j] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        r,c=len(matrix),len(matrix[0])
        rowstofill, colstofill = set(),set()
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    rowstofill.add(i)
                    colstofill.add(j)
        for row in rowstofill:
            for j in range(c):
                matrix[row][j]=0
                
        for col in colstofill:
            for i in range(r):
                matrix[i][col]=0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False
        # Check if first row or column has zero and set markers
        for row in range(rows):
            if matrix[row][0] == 0:
                first_col_has_zero = True
                break 
        for col in range(cols):
            if matrix[0][col] == 0:
                first_row_has_zero = True
                break
        # Mark zeros on the first row and column
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = matrix[0][col] = 0
        # Use markers to set zeros in the matrix
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
        
        # Step 4: Set zeros for the first row if needed
        if first_row_has_zero:
            for col in range(cols):
                matrix[0][col] = 0
        
        # Step 5: Set zeros for the first column if needed
        if first_col_has_zero:
            for row in range(rows):
                matrix[row][0] = 0