class TimeMap:

    def __init__(self):
        self.Store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.Store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        left, right = 0, len(self.Store[key]) - 1
        result = ""
        while left <= right:
            mid = left + (right - left) // 2
            if self.Store[key][mid][0] == timestamp:
                return self.Store[key][mid][1]
            elif self.Store[key][mid][0] < timestamp:
                result = self.Store[key][mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return result