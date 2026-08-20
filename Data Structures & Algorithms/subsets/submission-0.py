class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(nums, sub, i):
            if i == n:
                res.append(sub[:])
                return
            
            sub.append(nums[i])
            dfs(nums, sub, i+1)
            sub.pop()
            dfs(nums, sub, i+1)

        dfs(nums, [], 0)
        return res