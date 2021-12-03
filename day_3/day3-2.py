file = open("day_2_input.txt", "r")

data = file.read().strip().split("\n")
   
for line in data:
    print(line)
        
file.close()