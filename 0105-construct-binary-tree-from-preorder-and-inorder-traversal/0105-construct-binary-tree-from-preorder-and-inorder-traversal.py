# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_index = 0

        inorder_map = {}

        for i,value in enumerate(inorder):

            inorder_map[value] = i

        def dfs(left,right):

            nonlocal preorder_index

            if left > right:
                return None

            root_value = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_value)

            mid = inorder_map[root_value]

            root.left = dfs(left , mid-1)
            root.right = dfs(mid+1 , right)

            return root

        return dfs(0, len(inorder)-1 )
