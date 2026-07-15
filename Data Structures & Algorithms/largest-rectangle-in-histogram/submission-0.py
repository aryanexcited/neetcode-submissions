class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        maxArea = 0
        heights.append(0)
        
        for  i in range(len(heights)):
            while len(st) > 0 and heights[i] < heights[st[-1]]:
                poppedEle = st.pop()
                if not st:
                    left = -1
                else:
                    left = st[-1]
                maxArea = max(maxArea,(i-left-1)*heights[poppedEle])
            st.append(i)
        
        return maxArea