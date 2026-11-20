# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode | None, t2: TreeNode | None) -> TreeNode | None:
        if not t1:
            return t2
        elif not t2:
            return t1
        else:
            res = TreeNode(t1.val + t2.val)
            res.left = self.mergeTrees(t1.left, t2.left)
            res.right = self.mergeTrees(t1.right, t2.right)
        return res

# This one I had to look up. Couldn't really grasp how we
# have to work with this one. Turns out, the solution really was
# following the same logic as in the previous problems, but also
# turned out to be really elegant or, rather, laconic.

# We have conditions for not having one of the trees (it also works
# when a node has only one child), and after that - we use recursion
# once more. All values that are on the same node position in both
# trees get summed and written to a new resulting tree, that we'll
# return in the end.

# Both time and space are O(n) once again. We go through both trees
# at the same time and create a new one, which grows in size based
# on the original two.