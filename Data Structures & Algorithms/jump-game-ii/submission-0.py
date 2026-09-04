class Solution:
    def jump(self, nums: List[int]) -> int:
        reach, jumps, end = 0, 0, 0

        n = len(nums)
        for i in range(n-1):
            reach = max(reach, i + nums[i])
            if i == end:
                jumps += 1
                end = reach

        
        return jumps