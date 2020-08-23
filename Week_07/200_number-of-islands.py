from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        class UnionFind:

            def __init__(self, n):
                self.count = n
                self.parent = [i for i in range(n)]
                self.rank = [1 for _ in range(n)]   #每棵树的重量

            def get_count(self):
                return self.count

            def find(self, p):
                #找这个点的树的最上面的top root
                while p != self.parent[p]:
                    # 进行路径压缩
                    self.parent[p] = self.parent[self.parent[p]]
                    p = self.parent[p]
                return p

            def is_connected(self, p, q):
                return self.find(p) == self.find(q)

            def union(self, p, q):
                p_root = self.find(p)
                q_root = self.find(q)
                if p_root == q_root:
                    return

                # 如果p的重量大于q的重量，就将q挂载到p上
                if self.rank[p_root] > self.rank[q_root]:
                    self.parent[q_root] = p_root
                elif self.rank[p_root] < self.rank[q_root]:
                    self.parent[p_root] = q_root
                else:
                    self.parent[q_root] = p_root
                    self.rank[p_root] += 1

                # 经过上面合并操作，数量-1
                self.count -= 1

        row = len(grid)
        # 特判
        if row == 0:
            return 0
        col = len(grid[0])

        # 将二维数组打平成一维
        def get_index(x, y):
            return x * col + y

        # 注意：我们不用像 DFS 和 BFS 一样，4 个方向都要尝试，只要看一看右边和下面就可以了
        #只要往右边和下边进行尝试，纵向是x，横向是y(理解为第一坐标系顺时针旋转90°)
        directions = [(1, 0), (0, 1)]
        # 多开一个空间，把水域 "0" 都归到这个虚拟的老大上 水的top_root
        dummy_node = row * col

        # 多开的空间是虚拟的空间 这样初始总共有(n * m + 1)个树
        uf = UnionFind(dummy_node + 1)
        for i in range(row):
            for j in range(col):
                # 如果是水域，都连到那个虚拟的空间去
                if grid[i][j] == '0':
                    # 将第 i*col + j个挂载到dummy_root上
                    uf.union(get_index(i, j), dummy_node)
                if grid[i][j] == '1':
                    # 向下向右如果都是陆地，即 "1"，就要合并一下
                    for direction in directions:
                        new_x = i + direction[0]
                        new_y = j + direction[1]
                        if new_x < row and new_y < col and grid[new_x][new_y] == '1':
                            uf.union(get_index(i, j), get_index(new_x, new_y))
        # 减掉多出来的存水的dummy_root
        return uf.get_count() - 1