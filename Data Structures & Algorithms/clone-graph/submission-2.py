"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: 
            return None
        
        adjList = defaultdict(list)
        adjList[node] = Node(node.val)
        
        q = deque([node])

        while q: 
            current = q.popleft()

            for n in current.neighbors: 
                if n not in adjList:
                    adjList[n] = Node(n.val)
                    q.append(n)
                adjList[current].neighbors.append(adjList[n])

        return adjList[node]

