class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # construct an adjancency list
        adjList = defaultdict(list)
        for course, prereq in prerequisites: 
            adjList[course].append(prereq)
        
        # Depth first search
        visited = set()

        def dfs(course):
            if course in visited: return False
            if adjList[course] == []: return True

            visited.add(course)
            for p in adjList[course]:
                if not dfs(p): return False
            
            adjList[course] = []
            # remove from visited set why?
            visited.remove(course)
            return True
        
        for c, p in prerequisites:
            if not dfs(c): return False
        return True

