# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
                return True
        if not root or not subRoot:
            return False

        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        q = deque([root])
        while q:
            curr = q.pop()
            if curr.val == subRoot.val:
                if isSameTree(curr, subRoot):
                    return True
            
            if curr.right:
                q.append(curr.right)
            if curr.left:
                q.append(curr.left)

        return False