class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: 
            return 0
        
        l, r = 0, len(height)-1
        rightmax, leftmax = height[r], height[l]
        res = 0
        while l < r:
            if leftmax < rightmax:
                l += 1
                leftmax = max(height[l],leftmax)
                res += leftmax - height[l]
            else:
                r -= 1
                rightmax = max(height[r], rightmax)
                res += rightmax - height[r]
        
        return res