class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        scopy = [char.lower() for char in s if char.isalnum()]
        right = len(scopy)-1
        while left < right:
            if scopy[left]!=scopy[right]:
                return False
            left += 1
            right -= 1
        return True