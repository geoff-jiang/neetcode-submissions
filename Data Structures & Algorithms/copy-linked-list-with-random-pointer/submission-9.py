"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeDict = {None: None}

        if not head:
            return head

        curr = head
        while curr: 
            nodeDict[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            nodeDict[curr].random = nodeDict[curr.random]
            nodeDict[curr].next = nodeDict[curr.next]
            curr = curr.next
        
        return nodeDict[head]




