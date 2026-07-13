class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        st = deque()
        st.append(s[0])
        for i in range(1, len(s)):
            if len(st) > 0 and st[-1] == "{" and s[i] == "}":
                st.pop()
            elif len(st) > 0 and st[-1] == "[" and s[i] == "]":
                st.pop()
            elif len(st) > 0 and st[-1] == "(" and s[i] == ")":
                st.pop()
            else:
                st.append(s[i])

        if len(st) == 0:
            return True
        
        return False