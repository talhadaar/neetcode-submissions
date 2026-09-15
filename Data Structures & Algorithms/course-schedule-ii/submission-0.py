class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        for nxt,pre in prerequisites:
            indegree[nxt]+=1
            adj[pre].append(nxt)

        res = []

        def dfs(node):
            res.append(node)
            indegree[node]-=1
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    dfs(nei)

        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i)

        return res if len(res) == numCourses else []