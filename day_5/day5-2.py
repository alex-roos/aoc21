def build_vent_diagram(vent_list):
    build_list = []
    for row in range(1000):
        build_list.append([0]*1000)

    for coord_pair in vent_list:
        if coord_pair[1][0] > coord_pair[0][0]:
            _x1, _y1 = coord_pair[0]
            _x2, _y2 = coord_pair[1]
        else:
            _x1, _y1 = coord_pair[1]
            _x2, _y2 = coord_pair[0]

        # print(f"x1: {_x1}, y1: {_y1}")
        # print(f"x2: {_x2}, y2: {_y2}")

        # check horizontal line
        if _y1 == _y2:
            for col in range(_x1, _x2 + 1):
                build_list[_y1][col] += 1
        elif _x1 == _x2:
            for row in range(min(_y1, _y2), max(_y1, _y2) + 1):
                build_list[row][_x1] += 1
        else:  # diagonal
            if _y2 > _y1:
                # x1, y1 upper left to bottom right x2, y2
                curr_x = _x1
                for row in range(_y1, _y2 + 1):
                    build_list[row][curr_x] += 1
                    curr_x += 1
            else:
                # x1, y1 lower left to upper right x2, y2
                curr_x = _x2
                for row in range(_y2, _y1 + 1):
                    build_list[row][curr_x] += 1
                    curr_x -= 1

        # for i in range(len(build_list)):
        #     for j in range(len(build_list)):
        #         print(build_list[i][j]," ", end='')
        #     print()
        
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

count_high = 0

for i in range(len(vent_density)):
    for j in range(len(vent_density)):
        if vent_density[i][j] >= 2:
            count_high += 1

print(f"Those above 1: {count_high}")

file.close()