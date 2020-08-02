import collections

class Solution:
    def levelOrder(self,root):
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            # 这一层的元素长度
            size = len(queue)
            level = []
            for _ in range(size):
                cur = queue.popleft()
                if not cur:
                    continue
                level.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            if level:
                res.append(level)
        return res