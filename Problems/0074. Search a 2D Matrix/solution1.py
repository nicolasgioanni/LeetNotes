class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        rowT, rowB, colL, colR = 0, rows - 1, 0, cols - 1

        while rowT <= rowB:
            rowM = rowT + (rowB - rowT) // 2

            if matrix[rowM][colL] > target:
                rowB = rowM - 1
            elif matrix[rowM][colR] < target:
                rowT = rowM + 1
            else:
                while colL <= colR:
                    colM = colL + (colR - colL) // 2

                    if matrix[rowM][colM] < target:
                        colL = colM + 1
                    elif matrix[rowM][colM] > target:
                        colR = colM - 1
                    else:
                        return True
        return False
