class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)

        for start, end in edges:
            adjList[start].append(end)
            adjList[end].append(start)
        
        visited = set()
        def dfs(curr, parent):
            if curr in visited:
                return 
            visited.add(curr)

            for c in adjList[curr]:
                if c != parent:
                    dfs(c, curr)
        
        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                res += 1
        return res