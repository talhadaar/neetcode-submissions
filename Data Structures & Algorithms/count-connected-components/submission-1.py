class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list
        # Keep a visited list dict
        # Run DFS, each DFS run will be 1 connected component
        # For unvisited nodes, run DFS
        # Run untill all are visited
        # if we visit all in 1 pass, it is 1 fully connected component

        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(node):
            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        components = 0
        for node in range(n):
            if node not in visited:
                components+=1
                visited.add(node)
                dfs(node)

        return components