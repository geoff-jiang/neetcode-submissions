class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort? 
        indegrees = [0] * numCourses

        adjList = defaultdict(list)

        for course, prereq in prerequisites: 
            indegrees[course] += 1
            adjList[prereq].append(course)

        queue = deque(i for i in range(len(indegrees)) if indegrees[i] == 0 )

        taken = 0

        while queue: 
            curr = queue.popleft()

            taken += 1  

            for p in adjList[curr]: 
                indegrees[p] -= 1
                if indegrees[p] == 0:
                    queue.append(p) 
        return taken == numCourses