file = open("day_1_input.txt", "r")

data = file.read().split("\n")

windows = []

count = 0

for idx in range(0,len(data)-2):
    windows.append(int(data[idx]) + int(data[idx+1]) + int(data[idx+2]))
    
for window_idx in range(0, len(windows)-1):
    if windows[window_idx+1] > windows[window_idx]:
        count += 1
    
print(count)

file.close()