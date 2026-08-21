class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        def sub(subs, i):
            if i == n:
                res.append(subs[:])
                return
            
            subs.append(nums[i])
            sub(subs, i+1)
            while i<n-1 and nums[i] == nums[i+1]:
                i += 1
            subs.pop()
            sub(subs, i+1)
        
        sub([], 0)
        return res