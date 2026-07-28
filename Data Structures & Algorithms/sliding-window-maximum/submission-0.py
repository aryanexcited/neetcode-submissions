class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        helperSt = deque()
        result = []
        for i in range(len(nums)):
            while helperSt and nums[helperSt[-1]] <= nums[i]:
                helperSt.pop()
            while helperSt and helperSt[0] <= i-k:
                helperSt.popleft()
            helperSt.append(i)
            if i >= k-1:
                result.append(nums[helperSt[0]])
        
        return result