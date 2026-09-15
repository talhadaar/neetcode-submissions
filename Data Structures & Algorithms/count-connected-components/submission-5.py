class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # count(components) == DFS runs
        
        visited = [False] * n
        components = 0

        adj = defaultdict(list)
        for ai,bi in edges:
            adj[ai].append(bi)
            adj[bi].append(ai)

        def dfs(i):
            for nei in adj[i]:
                if not visited[nei]:
                    visited[nei]=True
                    dfs(nei)

        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(node)
                components+=1
        return components