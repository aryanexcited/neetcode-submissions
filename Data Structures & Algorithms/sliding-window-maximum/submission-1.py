class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        helperSt = deque()
        ans = []

        for i in range(len(nums)):
            while helperSt and nums[helperSt[-1]] <= nums[i]:
                helperSt.pop()
            
            helperSt.append(i)
            while helperSt and helperSt[0] < i - k + 1:
                helperSt.popleft()

            if i >= k - 1:
                ans.append(nums[helperSt[0]])
        
        return ans