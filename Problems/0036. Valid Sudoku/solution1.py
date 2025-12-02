class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value == ".":
                    continue
                
                boxID = (row // 3) + (col // 3) * 3
                
                if (value in rows[row] or
                    value in cols[col] or 
                    value in boxes[boxID]):
                    return False

                rows[row].add(value)
                cols[col].add(value)
                boxes[boxID].add(value)

        return True
