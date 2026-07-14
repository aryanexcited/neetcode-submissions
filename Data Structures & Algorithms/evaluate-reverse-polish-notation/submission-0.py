class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = deque()

        operators = {"*", "-", "+", "/"}

        for token in tokens:
            if token in operators and len(st)>=2:
                if token == "+":
                    num1 = st.pop()
                    num2 = st.pop()
                    res = num1 + num2
                    st.append(res)
                
                elif token == "-":
                    num1 = st.pop()
                    num2 = st.pop()
                    res = num2 - num1
                    st.append(res)

                elif token == "*":
                    num1 = st.pop()
                    num2 = st.pop()
                    res = num1 * num2
                    st.append(res)

                else:
                    num1 = st.pop()
                    num2 = st.pop()
                    res = num2 / num1
                    st.append(int(res))
            else:
                st.append(int(token))

        return st.pop()