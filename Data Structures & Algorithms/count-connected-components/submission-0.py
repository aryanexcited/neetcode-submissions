class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adjGraph = defaultdict(list)
        for [a, b] in edges:
            adjGraph[a].append(b)
            adjGraph[b].append(a)

        visited = set()
        count = 0

        def dfs():
            nonlocal count

            for i in range(n):
                if i in visited:
                    continue
                
                count += 1
                stack = [i]

                while stack:
                    node = stack.pop()
                    if node in visited:
                        continue
                    
                    visited.add(node)
                    for neighbors in adjGraph[node]:
                        stack.append(neighbors)

            return count

        return dfs()