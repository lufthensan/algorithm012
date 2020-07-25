class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if None is root:
            return 0

        children = [root.left,root.right]
        if not any(children):
            return 1

        # 先设置为无穷
        min_dept = float('inf')
        for c in children:
            if c:
                min_dept = min(self.minDepth(c),min_dept)
        return min_dept +1