class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n=len(s)

        def isPalin(s):
            left = 0
            right = len(s)-1
            while (left < right):
                if s[left]!=s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        def pp(sub,i):
            if i == n:
                res.append(sub[:])
                return 
            
            for j in range(i+1, n+1):
                if isPalin(s[i:j]):
                    sub.append(s[i:j])
                    pp(sub,j)
                    sub.pop()
        
        pp([], 0)
        return res