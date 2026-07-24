class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxFreq = 0
        freq = [0]*26
        left = 0
        right = 0
        for right in range(len(s)):
            freq[ord(s[right])-ord('A')] += 1
            maxFreq = max(maxFreq,freq[ord(s[right])-ord('A')])
            if (right - left + 1) - maxFreq > k:
                freq[ord(s[left])-ord('A')] -= 1
                left = left+1

        return right-left+1