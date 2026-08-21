class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []

        cars = list(zip(position,speed))
        cars.sort(reverse=True)
        n = len(cars)
        for i in range(n):
            time = (target - cars[i][0]) / cars[i][1]
            if not st or st[-1] < time:
                st.append(time)
            else:
                continue
        
        return len(st)