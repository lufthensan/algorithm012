class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:       
        n = len(grid)
        if not grid or grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        elif n <= 2:
            return n

        # 启发算法，往目标靠，哪边差得多，下一步就走哪边
        def heuristic(x, y):
            return max(abs(n-1 - x), abs(n-1 - y))
        #不太理解h干嘛的
        h = []
        heapq.heappush(h,(0, (0, 0, 1)))
        visited = set()
        while h:
            #按照权重取出，大的会先取出，所以heuristic是取max
            _, (i, j, step) = heapq.heappop(h)

            if (i, j) in visited:
                continue
            visited.add((i, j))

            for dx, dy in [(-1,-1), (1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1)]:
                next_i, next_j = i+dx, j+dy
                #下一步就到目的地了
                if next_i == n - 1 and next_j == n - 1:
                    return step + 1
                #如果在边界内，且下一步为0
                if 0 <= next_i < n and 0 <= next_j < n and grid[next_i][next_j] == 0:
                    # step+heuristic是优先级
                    heapq.heappush(h, (step + heuristic(next_i, next_j), (next_i, next_j, step+1)))

        return -1

