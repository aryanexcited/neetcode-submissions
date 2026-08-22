class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "1": {""},
            "2": {"a","b","c"},
            "3": {"d","e","f"},
            "4": {"g","h","i"},
            "5": {"j","k","l"},
            "6": {"m","n","o"},
            "7": {"p","q","r","s"},
            "8": {"t","u","v"},
            "9": {"w","x","y","z"},
            "0": {""}
        }

        n = len(digits)
        if n == 0:
            return []
        res = []

        def pp(sub, i):
            if i == n:
                res.append(sub)
                return
            
            for char in phone[digits[i]]:
                pp(sub+char, i+1)
            
        pp("", 0)
        return res