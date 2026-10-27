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
        nodeDict = defaultdict(lambda: Node(0))
        nodeDict[None] = None

        cur = head
        while cur: 
            nodeDict[cur].val = cur.val
            nodeDict[cur].next = nodeDict[cur.next]
            nodeDict[cur].random = nodeDict[cur.random]
            cur = cur.next
        
        return nodeDict[head]


    




