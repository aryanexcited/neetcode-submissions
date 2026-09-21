class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n-1:
            return False

        adjGraph = defaultdict(list)
        for [a,b] in edges:
            adjGraph[a].append(b)
            adjGraph[b].append(a)
        
        visited = set()
        def dfs():
            stack = [0]
            while stack:
                node = stack.pop()
                if node in visited:
                    continue
                
                visited.add(node)
                for neighbor in adjGraph[node]:
                    stack.append(neighbor)

        dfs()
        if len(visited) == n:
                return True

        return False