# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root,curr):
            if root is None:
                return 0

            curr = curr * 10 + root.val

            if root.right is None and root.left is None:
                return curr

            leftsum = dfs(root.left, curr)
            rightsum = dfs(root.right , curr)

            return leftsum + rightsum

        return dfs(root,0)
        

        