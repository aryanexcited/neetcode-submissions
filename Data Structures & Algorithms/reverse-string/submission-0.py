class Solution:
    def reverseString(self, s: List[str]) -> None:
        j = len(s)-1
        i = 0
        while i <= j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            j -= 1
            i += 1