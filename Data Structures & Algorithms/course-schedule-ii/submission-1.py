class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        unlocks = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            unlocks[prereq].append(course)
            indegree[course] += 1

        q = deque(c for c in range(numCourses) if indegree[c] == 0)
        order = []
        while q:
            prereq = q.popleft()
            order.append(prereq)
            for course in unlocks[prereq]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)

        return order if len(order) == numCourses else []