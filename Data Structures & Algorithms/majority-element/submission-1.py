class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorityElement = nums[0]
        vote = 0
        n = len(nums)
        for i in range(n):
            if vote == 0:
                    majorityElement = nums[i]
            if nums[i] == majorityElement:
                vote += 1
            else:
                vote-=1
        
        return majorityElement