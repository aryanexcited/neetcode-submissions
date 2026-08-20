class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = deque()
        operators = {"*","/","+","-"}
        for token in tokens:
            if token in operators:
                num1 = st.pop()
                num2 = st.pop()

                if token == "+":
                    st.append(num2+num1)
                
                elif token == "-":
                    st.append(num2-num1)
                
                elif token == "*":
                    st.append(num2*num1)
                
                else:
                    st.append(int(num2/num1))
                
            else:
                st.append(int(token))
            
        return st[-1]