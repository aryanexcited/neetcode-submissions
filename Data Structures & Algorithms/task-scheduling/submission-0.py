class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_map = Counter(tasks)
        max_freq = max(freq_map.values())
        k = 0 
        for val, freq in freq_map.items():
            if freq == max_freq:
                k += 1
        
        return max(((n+1)*(max_freq-1)+k),len(tasks))