class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if None is root:
            return 0
        right_height = self.maxDepth(root.right)
        left_height = self.maxDepth(root.left)
        return max(right_height,left_height)