class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = defaultdict(int)
        for i in range(len(nums)):
            hash[nums[i]] += 1

        for num,freq in hash.items():
            if freq > 1:
                return True

        return False