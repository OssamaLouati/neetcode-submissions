class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        """
        # 4, 1, 0, 7.   -> pos
        # 2, 2, 1, 1    -> speed

        time for car 1 to reach = 10 - 4 = 6/  2  = 3
        time for car 2 to reach = 10 - 1 = 9/  1  = 4,5
        
        time for car 3 to reach = 10 - 0 = 10/ 1  = 10
        time for car 4 to reach = 10 - 7 = 3/  1  = 3


        (0,1) (1,0) (4,2) (7,1)
        10     4,5    3     3
        """

        n = len(position)
        pos_time = []

        for i in range(n):
            time_left =  (target - position[i]) / speed[i]
            pos_time.append((position[i], time_left))

        pos_time.sort(key= lambda x : x[0], reverse=True)

        
        fleets = 0
        fleet_time = 0
        for _, time_left in pos_time:
            if time_left > fleet_time:
                fleet_time = time_left
                fleets +=1

        return fleets


        
    

        