class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0]*len(temperatures)

        st.append(0)

        for i in range(1, len(temperatures)):
            currTemp = temperatures[i]
            while len(st) >= 1 and temperatures[st[-1]] < currTemp:
                poppedInd = st.pop()
                res[poppedInd] = (i-poppedInd)
            st.append(i)
        
        return res