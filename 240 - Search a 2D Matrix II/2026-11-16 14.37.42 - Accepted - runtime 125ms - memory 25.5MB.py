class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        if not matrix:
            return False
        
        r = 0
        c = len(matrix[0]) - 1  # start top-right
        
        while r < len(matrix) and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1  # too big, go left
            else:
                r += 1  # too small, go down
        
        return False