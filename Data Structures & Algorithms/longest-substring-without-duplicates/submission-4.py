class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        window = set()
        res = 0 
        n = len(s)
        for r in range(n):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            res = max(res,len(window))
        return res