class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n-1:
            return False

        adjGraph = defaultdict(list)
        for [a,b] in edges:
            adjGraph[a].append(b)
            adjGraph[b].append(a)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for neighbor in adjGraph[node]:
                dfs(neighbor)

        dfs(0)
        if len(visited) == n:
                return True

        return False