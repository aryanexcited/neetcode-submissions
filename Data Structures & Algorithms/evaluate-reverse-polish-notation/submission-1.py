class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = deque()

        operators = {"*", "-", "+", "/"}

        for token in tokens:
            if token in operators and len(st)>=2:
                num1 = st.pop()
                num2 = st.pop()
                if token == "+":
                    res = num1 + num2
                
                elif token == "-":
                    res = num2 - num1

                elif token == "*":
                    res = num1 * num2

                else:
                    res = int(num2 / num1)
                st.append(res)
            else:
                st.append(int(token))

        return st.pop()