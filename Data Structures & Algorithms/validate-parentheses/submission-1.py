class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        st = deque()
        n = len(s)
        for i in range(n):
            if st and st[-1] == "(" and s[i] == ")":
                st.pop()
            elif st and st[-1] == "{" and s[i] == "}":
                st.pop()
            elif st and st[-1] == "[" and s[i] == "]":
                st.pop()
            else:
                st.append(s[i])
        
        return not bool(len(st))