class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash_s = defaultdict(int)

        for i in range(len(s)):
            hash_s[s[i]] += 1
        
        for i in range(len(t)):
            hash_s[t[i]] -= 1

        for ch,freq in hash_s.items():
            if freq > 0:
                return False

        return True