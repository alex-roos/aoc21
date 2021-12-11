file = open("day_8_input.txt", "r")
data = file.read().strip().split("\n")


_num_configs = {2: 1,   # 2 segments is the number one
                3: 7,   # 3 segments is the number seven
                4: 4,   # 4 segments is the number four
                7: 8}   # 7 segments is the number eight

count = 0

for line in data:
    left, right = line.strip().split("|")
    right_values = right.strip().split(" ")

    for _seq in right_values:
        if len(_seq) in _num_configs:
            count+=1

print(count)

file.close()