from math import ceil

class Solution:
    def hours(self,piles,k):
        ans = 0
        for i in range(len(piles)):
            ans += ceil(piles[i]/k)
        return ans

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1

        while left <= right:
            mid = left + (right - left) // 2
            ans = self.hours(piles,mid)
            if ans <= h:
                right = mid-1
            elif ans > h:
                left = mid+1

        return left