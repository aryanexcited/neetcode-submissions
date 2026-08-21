class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def gp(sub, cc, oc):
            if cc+oc == 2*n:
                res.append("".join(sub))
                return
            
            if oc < n:
                sub.append("(")
                gp(sub, cc, oc+1)
                sub.pop()

            if cc < oc:
                sub.append(")")
                gp(sub, cc+1, oc)
                sub.pop()

        
        gp([], 0, 0)
        return res