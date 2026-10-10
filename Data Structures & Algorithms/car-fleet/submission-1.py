class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # Step 1: Combine each car's position and speed into pairs.
        # Instead of a compact list comprehension, we use a standard loop.
        cars = []
        for i in range(len(position)):
            car_position = position[i]
            car_speed = speed[i]
            cars.append((car_position, car_speed))
            
        # Step 2: Sort the cars from the one closest to the target to the farthest.
        # reverse=True means the largest position comes first.
        cars.sort(reverse=True)
        
        # Step 3: Use a stack (a normal Python list) to store how much time 
        # each independent fleet takes to reach the finish line.
        stack = []
        
        # Step 4: Go through every car one by one
        for car in cars:
            p = car[0]  # car's position
            s = car[1]  # car's speed
            
            # Calculate how long this car takes to reach the target:
            # Time = Distance / Speed
            distance_to_go = target - p
            time_needed = distance_to_go / s
            
            # Add this car's time to our stack
            stack.append(time_needed)
            
            # Step 5: Check if we have at least 2 cars in the stack to compare.
            # stack[-1] is the current car we just added.
            # stack[-2] is the car right in front of it.
            if len(stack) >= 2:
                current_car_time = stack[-1]
                car_in_front_time = stack[-2]
                
                # If the car behind takes less time (or equal time) to reach the target
                # than the car in front of it, it will crash into it and join the same fleet.
                if current_car_time <= car_in_front_time:
                    # Remove it from the stack because it's part of the front car's fleet,
                    # not a new independent fleet.
                    stack.pop()
                    
        # Step 6: The total number of fleets is however many items are left in our stack.
        total_fleets = len(stack)
        return total_fleets
        