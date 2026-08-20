class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        n = len(nums)
        def cs(nums, subs, i):
            if sum(subs) == target:
                res.append(subs[:])
                return 
            elif i == n or sum(subs) > target:
                return
            
            subs.append(nums[i])
            cs(nums,subs,i)
            subs.pop()
            cs(nums,subs,i+1)
        
        cs(nums, sub, 0)
        return res