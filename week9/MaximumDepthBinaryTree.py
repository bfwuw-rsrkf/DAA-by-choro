# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return 1 + max(left_depth, right_depth)

# The idea in this algorithm is, well, recursive.
# The very thing that complicates the problem is the one
# we use to solve it. We return 1 for each node (if it is present,
# and if not - we return 0 right away), and then recursively call
# the function to calculate the depth of each subtree, then out
# of the two (if there are two, or even just one or none) we choose
# the one that's bigger to count (using Python's built-in function).
# That's the whole thing.

# The Time and Space complexities are both O(n) here, because we
# inevitably visit each node and create for each of the nodes two
# new variables.