# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return
        
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# We swap children! A horrible thing to do in the hospital,
# but not here - because we're implied to do so by the
# problem's conditions. Invertion means making every left
# child of a root right, and every right - left.

# So, we just do exactly that and just recursively call the
# function (of course, don't forget the base case - "nonexistent
# value"). Time and Space are both O(n), because we go through
# every node and create variables during each visit.