class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            current_prod = 1
            for j in range(len(nums)):
                if j != i:
                    current_prod *= nums[j]
            ans.append(current_prod)
        return ans