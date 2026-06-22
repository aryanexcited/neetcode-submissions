class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_s = defaultdict(int)

        n = len(s)
        for i in range(n):
            hash_s[s[i]] += 1

        for i in range(n):
            hash_s[t[i]] -= 1

        for _, freq in hash_s.items():
            if freq >= 1:
                return False

        return True
