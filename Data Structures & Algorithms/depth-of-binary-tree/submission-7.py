# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def getDepth(root, counter):
            if not root:
                return counter
            return max(getDepth(root.right, counter + 1), getDepth(root.left, counter + 1))
    
        return getDepth(root, 0)
            