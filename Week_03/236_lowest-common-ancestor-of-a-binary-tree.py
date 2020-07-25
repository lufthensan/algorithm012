class Solution:
    def lowestCommonAncestor(self,root:'TreeNode',p:'TreeNode',q:'TreeNode') -> 'TreeNode':
        # 如果其中一个是root节点的话，就直接返回root
        if not root or root ==p or root ==q:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if not left:return right
        if not right: return left
        return root