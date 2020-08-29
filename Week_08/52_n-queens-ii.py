class Solution:
    def __init__(self):
        self.count = 0

    def totalNQueens(self, n):
        if n < 1:
            return n
        self.DFS(0,0,0,0,n)
        return self.count;
    
    def DFS(self,row,col,pie,na,n):
        # 如果遍历深度大等于n，表明找到了一个新的解
        if row >= n:
            self.count += 1
            return
        
        # (col | pie | na)获取所有已经被占位的咧，区分就是可以放置皇后的咧
        # &((1 <<n ) -1)目的是排除高位的干扰，只取底n位，其他全置为0
        bits = (~(col | pie | na)) & ((1 << n) -1);
        # bits二进制中1就表示可以放置皇后 != 0表示二进制有1
        while bits != 0:
            # 获取最后一个1
            p = bits & (-bits)
            # (col|p)在bit位放置了1，则其他列不能再放置在该位置
            # (pie|p)<< 1：下一行收到/攻击而不能放置的列
            # (na|p)>>>1:下一行因为收到\攻击而不能放置的列
            # \使用>>>无符号位移，当n=32时，第一行第一列会被认为是负号
            self.DFS(row+1,col|p,(pie|p)<<1,(na|p)>>1,n)
            # 在p的位置上放置皇后
            bits = bits & (bits -1)