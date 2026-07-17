class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1

        while left <= right:
            ans = 0
            mid = left + (right - left) // 2
            for pile in piles:
                ans = ans + (pile + mid - 1) // mid
            if ans <= h:
                right = mid-1
            elif ans > h:
                left = mid+1

        return left