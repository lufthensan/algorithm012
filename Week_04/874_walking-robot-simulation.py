class Solution:
    def robotSim(self, commands, obstracles):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        # 和下面的di组合起来，dx dy组合成上下左右
        x = y = di = 0
        obstracles = set(map(tuple, obstracles))
        ans = 0

        for cmd in commands:
            if cmd == -2:  # left
                di = (di - 1) % 4
            if cmd == -1:
                di = (di + 1) % 4
            else:
                for k in range(cmd):
                    if (x + dx[di], y + dy[di]) not in obstracles:
                        x += dx[di]
                        y += dx[di]
                        ans = max(ans, x * x + y * y)
        return ans
