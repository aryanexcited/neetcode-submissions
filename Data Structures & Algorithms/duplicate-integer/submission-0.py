class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = defaultdict(int)
        n = len(nums)
        for i in range(n):
            hash[nums[i]]+=1

        for num,freq in hash.items():
            if freq > 1:
                return True

        return False