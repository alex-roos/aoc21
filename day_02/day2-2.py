file = open("day_2_input.txt", "r")

data = file.read().split("\n")
   
forward = 0
depth = 0

aim = 0

for movement in data:
    direction, dist = movement.split(" ")
    dist = int(dist)
    
    if direction == "forward":
        forward += dist
        depth += aim * dist
    elif direction == "down":
        aim += dist
    elif direction == "up":
        aim -= dist
        
print(forward * depth)

file.close()