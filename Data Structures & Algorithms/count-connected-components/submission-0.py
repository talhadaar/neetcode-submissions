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

        visited = [False] * n

        def bfs(node):
            q = deque([node])
            visited[node] = True
            while q:
                curr = q.popleft()
                for nei in adj[curr]:
                    if not visited[nei]:
                        visited[nei]=True
                        q.append(nei)

        components = 0
        for node in range(n):
            if not visited[node]:
                bfs(node)
                components+=1

        return components