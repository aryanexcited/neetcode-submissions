class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0

        freq_t = defaultdict()
        freq_window = defaultdict(int)

        freq_t = Counter(t)
        result = ""
        have = 0
        need = len(freq_t)
        best_len = float('inf')
        for r in range(len(s)):
            c = s[r]
            freq_window[c] += 1
            if freq_window[c] == freq_t[c]:
                have += 1
                while have == need:
                    if have == need and best_len > (r-l+1):
                        result = s[l:r+1]
                        best_len = (r-l+1)
                    freq_window[s[l]] -= 1
                    if freq_window[s[l]] < freq_t[s[l]]:
                        have -= 1
                    l += 1
        
        return result 