height_map = []
basin_map = []

def add_neighbors(_row, _col):
    neighbor_list = set()

    if _row > 0:
        neighbor_list.add((_row-1, _col))
    if _row < len(height_map) - 1:
        neighbor_list.add((_row+1, _col))
    if _col > 0:
        neighbor_list.add((_row, _col-1))
    if _col < len(height_map[0]) - 1:
        neighbor_list.add((_row, _col+1))

    return neighbor_list

def crawl_map(row_start, col_start, curr_zone):   
    count = 0

    to_visit = set()
    visited = set()

    to_visit = to_visit.union(add_neighbors(row_start, col_start))

    while len(to_visit) > 0:
        next_loc = list(to_visit)[0]
        visited.add(next_loc)
        to_visit.remove(next_loc)
        next_loc_val = basin_map[next_loc[0]][next_loc[1]]

        if next_loc_val != 99999 and next_loc_val < 0:
            basin_map[next_loc[0]][next_loc[1]] = curr_zone
            count += 1

            neighbors = add_neighbors(next_loc[0], next_loc[1])

            for n in neighbors:
                if n not in visited:
                    to_visit.add(n)

    # print(f"For {row_start}, {col_start} checking locations {to_visit}")
    # print(f"Current Value {height_map[row_start][col_start]}: against: ", end='')
    return count


file = open("day_9_input.txt", "r")
data = file.read().strip().split("\n")

for line in data:
    casted_line = [int(i) for i in line.strip()]
    height_map.append(casted_line)

    basin_line = []
    for item in casted_line:
        if item == 9:
            basin_line.append(99999)
        else:
            basin_line.append(-1)
    basin_map.append(basin_line)
    
risk_sum = 0
zone_count = 0

sizes = []

for r in range(len(height_map)):
    for c in range(len(height_map[0])):
        if basin_map[r][c] < 0:
            sizes.append(crawl_map(r, c, zone_count))
            zone_count += 1

sizes.sort(reverse=True)
print(sizes[0] * sizes[1] * sizes[2])

file.close()