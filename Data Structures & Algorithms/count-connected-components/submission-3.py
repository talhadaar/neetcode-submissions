class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # n nodes labelled 0 <= LABEL <= n-1
        # for 5 nodes, max labels are 0 to 4

        # Make adjacency matrix
        # keep a list of [-1]*(n-1)
        # Run DFS from root, add 

        adj = defaultdict(list)
        visited = [False] * n
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)

        componentes = 0
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(node)
                componentes+=1
        return componentes