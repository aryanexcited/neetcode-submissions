class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = defaultdict(int)

        for i in range(len(nums)):
            ans[nums[i]] += 1
        
        ans = sorted(ans.items
        (),  key=lambda x:x[1], reverse=True)

        return [items[0] for items in ans[:k]]