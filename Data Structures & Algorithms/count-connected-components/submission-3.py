class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graphs = defaultdict(list)

        # Build the graph
        for a,b in edges:
            graphs[a].append(b)
            graphs[b].append(a)

        visited = set()
        components = 0
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in graphs[node]:
                dfs(nei)

        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1 


        return components
        