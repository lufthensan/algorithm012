class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for i in range(9)]
        colums = [{} for i in range(9)]
        boxes = [{} for i in range(9)]
        for i in range(9):
            for j in range(9):
               num = board[i][j]
               if num != '.':
                   num = int(num)
                   box_index = (i//3) * 3+ j//3

                   rows[i][num] = rows[i].get(num,0)+1
                   colums[j][num] = colums[j].get(num,0)+1
                   boxes[box_index][num] = boxes[box_index].get(num,0) + 1

                   if rows[i][num] >1 or colums[j][num] >1 or boxes[box_index][num] > 1:
                       return False
        return True
            