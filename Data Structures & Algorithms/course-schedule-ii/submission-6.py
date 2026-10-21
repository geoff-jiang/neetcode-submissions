class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list) 

        indegrees = [0] * numCourses
        for course, pre in prerequisites: 
            adjList[pre].append(course)
            indegrees[course] += 1

        # {0: 1}
        
        queue = deque()
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)
        
        path = []

        while queue: 
            curr = queue.popleft()
            path.append(curr)
            for course in adjList[curr]:
                indegrees[course] -= 1
                if indegrees[course] == 0:
                    queue.append(course)
        return path if len(path) == numCourses else []

