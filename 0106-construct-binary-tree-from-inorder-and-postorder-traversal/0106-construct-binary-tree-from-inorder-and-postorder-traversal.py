# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        postorder_index = len(postorder) - 1

        in_map = {}
        for i,value in enumerate(inorder):
            in_map[value] = i

        def dfs(left, right):

            nonlocal postorder_index 

            if left > right:
                return None

            root_value = postorder[postorder_index]

            postorder_index -= 1

            root = TreeNode(root_value)

            mid = in_map[root_value]

            root.right = dfs(mid+1 , right)
            root.left = dfs(left , mid-1)

            return root

        return dfs(0, len(inorder) - 1 )


        
