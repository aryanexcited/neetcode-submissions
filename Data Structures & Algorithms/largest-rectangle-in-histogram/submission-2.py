class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        heights.append(0)
        res = 0
        n = len(heights)
        for i in range(n):
            while st and heights[st[-1]] > heights[i]:
                j = st.pop()
                if not st:
                    left = -1
                else:
                    left = st[-1]
                res = max(res,(heights[j]*(i-left-1)))
            st.append(i)
        
        return res