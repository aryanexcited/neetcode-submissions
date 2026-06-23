class Solution:
    @staticmethod
    def shift_char(c, k):
        if 'a' <= c <= 'z':
            return chr((ord(c) - ord('a') + k) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            return chr((ord(c) - ord('A') + k) % 26 + ord('A'))
        else:
            return c  

    def encode(self, strs: List[str]) -> str:
        return "".join(str(len(s))+"#"+s for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j]!="#":
                j+=1
            length = int(s[i:j])
            res.append(s[j+1:j+length+1])
            i = j + 1 + length
        return res    
        