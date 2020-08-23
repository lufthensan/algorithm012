class Solution:

    

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        def dfs(board,i,j):
            if i<0 or j < 0 or i>= m or j>= n or board[i][j] == 'X' or board[i][j] =='#':
                return
            board[i][j] = '#'
            for direction in directions:
                dfs(board,i+direction[0],j+direction[1])
        
        if not len(board) or not board:
            return 
        
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                isEdge = i==0 or j==0 or i== m-1 or j==n-1
                if isEdge and board[i][j] == 'O':
                    dfs(board,i,j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'
        
       