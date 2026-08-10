class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Valid Tree: Fully connected, no cycles

        if len(edges) > n-1:
            return False

        # Make adjacency list
        adj=[[] for _ in range(n)]
        print(adj)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # traverse with bfs, if a visited edge is visited again
        # it has a cycle
        # if an edge has not been visited, 
        visited = set()
        # (curent node, parent node)
        # parent set to -1, to say that no parent existed.
        q = deque([(0,-1)])
        visited.add(0)

        while q:
            node, parent = q.popleft()
            # check each nei
            for nei in adj[node]:
                # edge [0,1] and [1,0] is the same in undirected graph
                # so we skip this duplicate edge
                if nei == parent:
                    continue
                # if we somehow returned to a visited node, we found a cycle
                if nei in visited:
                    return False

                visited.add(nei)
                q.append((nei, node))

        return len(visited) == n