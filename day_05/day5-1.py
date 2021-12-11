from os import pardir, pathsep


def build_vent_diagram(vent_list):
    build_list = []
    for row in range(999):
        build_list.append([0]*999)

    for coord_pair in vent_list:
        _x1, _y1 = coord_pair[0]
        _x2, _y2 = coord_pair[1]

        print(f"pair 1,  x: {_x1}, y: {_y1}")
        print(f"pair 2,  x: {_x2}, y: {_y2}")

        # check horizontal line
        if _y1 == _y2:
            for col in range(min(_x1, _x2), max(_x1, _x2) + 1):
                build_list[_y1][col] += 1
        elif _x1 == _x2:
            for row in range(min(_y1, _y2), max(_y1, _y2) + 1):
                build_list[row][_x1] += 1
        
    return build_list


file = open("day_5_input.txt", "r")
data = file.read().strip().split("\n")

# pairs of start end pairs
vents = []

for line in data[:]:
    parts = line.split(' ')

    # print(f"part 1 {parts[0]}")
    # print(f"part 2 {parts[2]}")

    x1 = int(parts[0].split(',')[0])
    y1 = int(parts[0].split(',')[1])
    x2 = int(parts[2].split(',')[0])
    y2 = int(parts[2].split(',')[1])
    #vents.append(((int(line[0],int(line[2])), (int(line[-3]), int(line[-1])))))

    vents.append(((x1, y1), (x2, y2)))

vent_density = build_vent_diagram(vents)

# for i in range(len(vent_density)):
#     for j in range(len(vent_density)):
#         print(vent_density[i][j], end='')
#     print()

count_high = 0

for i in range(len(vent_density)):
    for j in range(len(vent_density)):
        if vent_density[i][j] >= 2:
            count_high += 1

print(f"Those above 1: {count_high}")

file.close()