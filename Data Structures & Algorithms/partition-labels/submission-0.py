class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_seen = defaultdict(int)
        n = len(s)
        for i in range(n):
            last_seen[s[i]] = i
        
        print(last_seen)
        
        ans = []
        start = 0
        end = 0
        for i in range(n):
            end = max(end, last_seen[s[i]])
            if i == end:
                ans.append(end - start + 1)
                start = i+1
        return ans