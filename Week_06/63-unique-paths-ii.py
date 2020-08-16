class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        height ,width = len(obstacleGrid),len(obstacleGrid[0])

        store = [[0] * width for i in range(height)]

        for m in range(height):
            for n in range(width):
                if not obstacleGrid[m][n]:
                    if m==n ==0:
                        store[m][n] = 1
                    else:
                        a = store[m-1][n] if m != 0 else 0
                        b = store[m][n-1] if n!=0 else 0    #左边格子
                        store[m][n] = a+b
        return store[-1][-1]