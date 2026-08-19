class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        hash_map = {key: 0 for key in range(min(nums),max(nums)+1)}

        for num in nums:
            hash_map[num] += 1
        
        result = []
        for num,freq in hash_map.items():
            if freq > 0:
                for _ in range(freq):
                    result.append(num)
        
        return result