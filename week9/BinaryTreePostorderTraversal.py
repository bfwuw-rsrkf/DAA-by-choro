# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            inorder(root.right)
            res.append(root.val)
        
        inorder(root)
        return res

# Same as in the previous two similar problems - we just change the order
# of the action. Space and Time complexities remain unchanged, of course.