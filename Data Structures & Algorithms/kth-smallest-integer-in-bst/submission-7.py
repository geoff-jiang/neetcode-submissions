# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        def inOrderTraversal(root):
            if not root:
                return
            inOrderTraversal(root.left)
            heapq.heappush(heap, root.val)
            inOrderTraversal(root.right)

        inOrderTraversal(root)
        print(heap)
        for i in range(k - 1):
            heapq.heappop(heap)
        return heapq.heappop(heap)
        

        

        