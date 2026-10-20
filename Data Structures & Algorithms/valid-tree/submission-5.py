class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # {
        #     0: [1],
        #     1: [2, 3, 4],
        #     2: [3]
        # }

        if len(edges) != n - 1:
            return False
            
        adjList = defaultdict(list)
        for start, end in edges:
            adjList[start].append(end)
            adjList[end].append(start)
        
        stack = [(0, -1)]
        # [curr, parent]
        visited = set()
        # (0 1 4 3 2)
        while stack: 
            curr, parent = stack.pop()
            if curr in visited: 
                return False
            visited.add(curr)

            for nei in adjList[curr]:
                if nei != parent:
                    stack.append((nei, curr))
        
        return len(visited) == n 

