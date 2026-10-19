# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(s1, s2):
            if not s1 and not s2:
                return True
            if not s1 or not s2 or s1.val != s2.val:
                return False
            
            return dfs(s1.left, s2.left) and dfs(s1.right, s2.right)
        
        return dfs(p, q)



