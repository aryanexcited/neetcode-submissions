class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        
        while left <= right:
            ans = 0
            mid = left + (right-left) // 2
            ans = sum(math.ceil(pile/mid) for pile in piles)
            if ans > h:
                left = mid + 1
            elif ans <= h:
                right = mid - 1
            else:
                break
        
        return left