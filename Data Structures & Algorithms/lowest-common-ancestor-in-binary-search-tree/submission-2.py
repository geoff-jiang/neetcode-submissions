# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # dictionary of nodes and parents
        ancestors = {root: None}

        queue = deque([root])

        while queue:
            if p in ancestors and q in ancestors:
                break 
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
                ancestors[curr.left] = curr
            if curr.right:
                queue.append(curr.right)
                ancestors[curr.right] = curr
        

        parentSet = set()
        parent = p
        while parent:
            parentSet.add(parent)
            parent = ancestors[parent]
        
        while q:
            if q in parentSet:
                return q
            q = ancestors[q]
        
        return None
        