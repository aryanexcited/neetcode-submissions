class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = defaultdict(int)
        hash[nums[0]] = 0
        i = 1
        for i in range(1,len(nums)):
            complement = target - nums[i]
            if complement in hash:
                break
            else:
                hash[nums[i]] = i
        return [hash[target-nums[i]],i]