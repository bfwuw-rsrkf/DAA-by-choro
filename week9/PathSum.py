# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right:
            return targetSum - root.val == 0
        
        targetSum -= root.val
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

# So, again, we search recursively. Because in the problem it is stated,
# that the path must be root-to-leaf, then before telling if the answer
# is true or false, we must first reach a leaf, so that's why we have
# the if condition on line 12.

# The approach is to just subtract from the targetSum while we are on
# our way "up the tree". If by the point we reach a leaf the targetSum is
# exactly 0, then the answer is true, because we basically got exactly the
# needed values along the way. By using the subtraction method, we don't
# have to create any additional variables and track them.

# The Time complexity is O(n), because we inevitably visit every single node
# to check for the path sum, and the Space is O(1), because we don't create
# anything new in the system.