# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []

        def inorder(root):
            if not root:
                return
            res.append(root.val)
            inorder(root.left)
            inorder(root.right)
        
        inorder(root)
        return res

# So, we solve this one just the same way as we did
# in the Inorder traversal. Suprisingly (for me, at least,
# personally), the traversal aren't that much different in
# code, but produce completely different results, and also 
# completely different visually.

# So, in here we just swap the "action" order, and ta-da:
# we get the solution.

# The time and space remain the same: O(n).