class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = set()
        res = []
        n = len(nums)
        def perm(nums, subs, used):
            if len(subs) == n:
                res.append(subs[:])
                return
            
            for ele in nums:
                if ele in used:
                    continue
                else:
                    used.add(ele)
                    subs.append(ele)
                    perm(nums, subs, used)
                    subs.pop()
                    used.remove(ele)
            
        perm(nums, [], used)
        return res