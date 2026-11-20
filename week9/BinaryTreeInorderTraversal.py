# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        
        inorder(root)
        return res

# I'll be honest, I knew that the code must've been
# recursive and make actions ("turns") in the order
# of the traversal way we needed. I knew how "turns"
# would've been implemented, but the "actions" weren't
# so clear, so I looked up the solution. I found a very
# nice explanation that said:
# -for Inorder, we do something between left and right.
# -for Preorder, we do something before left and right.
# -for Postorder, we do something after left and right.

# Both Space and Time are O(n). We go through all the
# elements of that tree, and we create a new "cell" for
# each of it.