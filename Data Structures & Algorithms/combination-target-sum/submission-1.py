class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        n = len(nums)
        def cs(nums, subs, i, sumArr):
            if sumArr == target:
                res.append(subs[:])
                return 
            elif i == n or sumArr > target:
                return
            
            sumArr+=nums[i]
            subs.append(nums[i])
            cs(nums,subs,i,sumArr)
            sumArr-=nums[i]
            subs.pop()
            cs(nums,subs,i+1,sumArr)
        
        cs(nums, sub, 0, 0)
        return res