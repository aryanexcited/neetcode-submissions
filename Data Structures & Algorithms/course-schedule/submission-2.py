class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)
        path = set()
        safe = set()

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
                    continue
                
                if node in safe:
                    continue
                
                if node in path:
                    return False
                
                path.add(node)
                stack.append((node,True))

                for neighbor in courses[node]:
                    if neighbor not in safe:
                        stack.append((neighbor,False))

        return True