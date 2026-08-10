class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = defaultdict(int)
        n = len(nums)
        for i in range(n):
            hash[nums[i]] += 1
        
        buckets = [[] for _ in range(len(nums)+1)]
        for value, freq in hash.items():
            buckets[freq].append(value)

        ans = []
        i = len(buckets)-1
        for i in range(len(nums), -1, -1):
            for ele in buckets[i]:
                ans.append(ele)
                k-=1
                if k == 0:
                    break
            if k == 0:
                break

        return ans