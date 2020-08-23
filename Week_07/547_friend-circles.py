class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # 并查集
        class UnionFind(object):
            def __init__(self,size):
                self.p = [i for i in range(size + 1)]
                self.num = size
            
            def find(self,x:int):
                # 路径压缩的并查集，压缩到第二级
                if self.p[x] != x:
                    self.p[x] = self.find(self.p[x])
                return self.p[x]
            
            def union(self,a:int,b:int):
                # 如果是两个不同的根，进行合并
                if self.find(a) != self.find(b):
                    self.p[self.find(a)] = self.p[self.find(b)]
                    self.num -= 1

        n = len(M)
        if n ==1:
            return 1
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i+1,n):
                # i j 其实就表示第i个人和第j个人合并
                if M[i][j]:
                    uf.union(i,j)
        return uf.num