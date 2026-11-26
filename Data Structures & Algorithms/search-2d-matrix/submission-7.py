class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            row = (top + bottom) // 2
            if matrix[row][0] > target:
                bottom = row - 1
            elif matrix[row][right] < target:
                top = row + 1
            else:
                break

        if top > bottom:
            return False

        valid_row = (top + bottom) // 2
        while left <= right:
            col = (left + right) // 2

            if matrix[valid_row][col] < target:
                left = col + 1
            elif matrix[valid_row][col] > target:
                right = col - 1
            else:
                return True

        return False