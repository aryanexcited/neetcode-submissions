class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = []

        cars = list(zip(position,speed))
        cars.sort(reverse=True)

        for position, speed in cars:
            time = (target-position)/speed
            if not res:
                res.append(time)
            
            elif res[-1] < time:
                res.append(time)
            
            else:
                continue
        
        return len(res)