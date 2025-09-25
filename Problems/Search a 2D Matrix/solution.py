class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rowT, rowB = 0, len(matrix) - 1
        colL, colR = 0, len(matrix[0]) - 1

        while rowT <= rowB:
            rowM = (rowT + rowB) // 2

            if target > matrix[rowM][colR]:
                rowT = rowM + 1
            elif target < matrix[rowM][colL]:
                rowB = rowM - 1
            else:
                
                while colL <= colR:
                    colM = (colL + colR) // 2

                    if target > matrix[rowM][colM]:
                        colL = colM + 1
                    elif target < matrix[rowM][colM]:
                        colR = colM - 1
                    else:
                        return True
        return False
