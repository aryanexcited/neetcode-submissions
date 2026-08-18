class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        res = 0
        maxLeft,maxRight = 0, 0
        while left <= right:
            if maxLeft < maxRight:
                maxLeft = max(maxLeft, height[left])
                res += max(maxLeft-height[left],0)
                left += 1
            else:
                maxRight = max(maxRight, height[right])
                res += max(maxRight-height[right],0)
                right -= 1
        return res