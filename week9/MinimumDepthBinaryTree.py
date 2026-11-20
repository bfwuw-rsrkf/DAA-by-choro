# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        
        if left_depth and right_depth:
            return 1 + min(left_depth, right_depth)
        else:
            return 1 + left_depth + right_depth

# The idea is absolutely the same as in the previous
# problem, except there are some differences:
# because we need the shortest path, when we return
# the "base-case" depth + the depth of the needed 
# subtree, we choose the shorter subtree.

# BUT because we now use the "min" function, it will
# choose the subtree that doesn't exist, because it
# will have the depth of 0, so we have to make an 
# if-else condition to avoid this situation.

# The time and space are the same as in the previous:
# O(n)