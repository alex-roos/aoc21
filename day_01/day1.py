file = open("day_1_input.txt", "r")

data = file.read().split("\n")

count = 0

for idx in range(len(data)):
    if idx < len(data)-1 and int(data[idx+1]) > int(data[idx]):
        count += 1
    
print(count)

file.close()