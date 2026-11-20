# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        def dfs(node, path, result):
            if not node:
                return
            path += str(node.val)
            if not node.left and not node.right:
                result.append(path)
            else:
                dfs(node.left, path + '->', result)
                dfs(node.right, path + '->', result)

        result = []
        dfs(root, '', result)
        return result 

# The whole problem gets complicated only because of one thing:
# we have to output the solution "with grace" ('->', seriously?)

# But other than that, nothing complicated. We store all paths in
# a result list, every path is just a String that gets stored in
# the list every time we reach a leaf (thus, the if condition on
# line 13), and we go back to abusing the recursion once again.
# Oh, and every variable has to be passed down to the next "iteration",
# of course.

# Both time and space are O(n). We visit each node and make modifications
# to the strings.