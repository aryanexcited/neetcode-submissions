class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = [0]*26
        freq2 = [0]*26
        winSize = len(s1)
        left = 0
        for i in range(winSize):
            freq1[ord(s1[i]) - ord('a')] += 1
        
        for right in range(len(s2)):
            freq2[ord(s2[right]) - ord('a')] += 1
            if (right-left+1) > winSize:
                freq2[ord(s2[left]) - ord('a')] -= 1
                left += 1
                if freq1 == freq2:
                    return True
            elif freq1 == freq2:
                return True

        return False