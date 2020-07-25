class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
       #定义一个内部方法Helper
        def helper(node,lower=float('-inf'),upper = float('inf')):
            #如果没有左节点或有节点，就不用校验
            if not node:
                return True

            val = node.val
            #值要在lr之间
            if val <= lower or val >= upper:
                return False

            # 右边节点值要在[root,upper之间
            if not helper(node.right,val,upper):
                return False
            # 左边节点值要在[lower,root之间
            if not helper(node.left,lower,val):
                return False
            return True
        return helper(root)