class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        fe = float('-inf')
        se = float('-inf')
        te = float('-inf')
        
        n = len(triplets)
        for i in range(n):
            if (triplets[i][0] <= target[0] and
                triplets[i][1] <= target[1] and
                triplets[i][2] <= target[2]):
                    fe = max(fe,triplets[i][0])
                    se = max(se,triplets[i][1])
                    te = max(te,triplets[i][2])
        
        res_triplet = [fe,se,te]
        if res_triplet == target:
            return True
        
        return False