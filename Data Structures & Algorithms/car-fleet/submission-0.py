class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        ans = n
        car = [(p, s) for p, s in zip(position, speed)]
        car.sort()

        for _ in range(n - 1):
            front_car = car.pop()
            back_car = car.pop()

            front_arrival = (target - front_car[0]) / front_car[1]
            diff_pos = front_car[0] - back_car[0]
            diff_speed = back_car[1] - front_car[1]

            if diff_speed > 0 and front_arrival >= (diff_pos / diff_speed):
                ans -= 1
                car.append(front_car)
            else:
                car.append(back_car)
        
        return ans