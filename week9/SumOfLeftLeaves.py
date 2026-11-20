# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        def f(root, isLeft=False):
            if not root: return 0
            if not root.left and not root.right and isLeft: return root.val
            return f(root.left, True)+f(root.right, False)

        return f(root)

# And yet again, we do the solution recursively. We actually
# go for each of the branches of the root, because even a right 
# branch might have a left one, which would end up having a left leaf
# or even being one, and our objective is to sum all the left leaves.
# We pass on "leftness" variable on each left subtree, and when reaching
# a leaf, we pass the leaf's value "down" the tree, "through" the recursion.

# Time? Again, O(n). We go through every node. Space? O(1). No anything new.