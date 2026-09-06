class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        n = len(hand)
        l = [0]*1001

        if n % groupSize != 0:
            return False

        for val in hand:
            l[val] += 1
        
        currStart = 0

        while currStart < 1001:
            if l[currStart] > 0:
                groups = l[currStart]
                s = currStart
                for i in range(groupSize-1, -1, -1):
                    if s + i > 1000 or l[s + i] < groups :
                        return False
                    l[s + i] -= groups
                    if l[s+i] > 0:
                        currStart = s+i
            else:
                currStart += 1

        return True