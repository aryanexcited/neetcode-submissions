class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = defaultdict(list)
        path = set()
        safe = set()
        order = []

        for a,b in prerequisites:
            courses[b].append(a)

        for start in range(numCourses):
            if start in safe:
                continue
            
            stack = [(start,False)]
            while stack:
                node, is_finalize = stack.pop()

                if is_finalize:
                    path.remove(node)
                    safe.add(node)
                    order.append(node)
                    continue
                
                if node in safe:
                    continue
                
                if node in path:
                    return []
                
                path.add(node)
                stack.append((node,True))

                for neighbor in courses[node]:
                    if neighbor not in safe:
                        stack.append((neighbor,False))

        return order[::-1]