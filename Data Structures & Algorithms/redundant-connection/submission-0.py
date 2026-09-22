class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))

        def find(x):
            while parent[x] != x:
                x = parent[x]
            
            return x
        
        def union(a,b):
            root_a = find(a)
            root_b = find(b)

            parent[root_b] = root_a
        
        for [a,b] in edges:
            if find(a) == find(b):
                return [a, b]
            
            union(a,b)