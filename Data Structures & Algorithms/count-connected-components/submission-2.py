class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        # build graph
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        components = 0
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in graph[node]:
                dfs(nei)
        for node in range(n):
            if node not in visited:
                dfs(node)
                components += 1
        return components


        