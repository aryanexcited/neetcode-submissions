class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank, current_tank, start = 0, 0, 0

        n = len(gas)
        for i in range(n):
            current_tank += gas[i] - cost[i]
            if current_tank < 0:
                start = i+1
                current_tank = 0
            total_tank += gas[i] - cost[i]

        if total_tank >= 0:
            return start
        
        return -1