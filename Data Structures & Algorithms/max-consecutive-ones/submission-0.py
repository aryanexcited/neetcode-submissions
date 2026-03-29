class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        tempCount = 0
        for i in range(0,len(nums)):
            if nums[i] == 1:
                tempCount+=1

            else:
                count = max(count,tempCount)
                tempCount = 0
        
        count = max(count, tempCount)
        return count