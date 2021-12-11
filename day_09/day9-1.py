heightmap = []

def is_local_min(row, col):
    found_lower_val = False
    
    check_locs = set()

    if row > 0:
        check_locs.add((row-1, col))
    if row < len(heightmap) - 1:
        check_locs.add((row+1, col))
    if col > 0:
        check_locs.add((row, col-1))
    if col < len(heightmap[0]) - 1:
        check_locs.add((row, col+1))

    print(f"For {row}, {col} checking locations {check_locs}")
    print(f"Current Value {heightmap[row][col]}: against: ", end='')
    for loc in check_locs:
        print(f"{heightmap[loc[0]][loc[1]]}, ", end='')
        if heightmap[row][col] >= heightmap[loc[0]][loc[1]]:
            found_lower_val = True
    print()
    return not found_lower_val


file = open("day_9_input.txt", "r")
data = file.read().strip().split("\n")

for line in data:
    heightmap.append([int(i) for i in line.strip()])

risk_sum = 0

for r in range(len(heightmap)):
    for c in range(len(heightmap[0])):
        if is_local_min(r, c):
            risk_sum += 1 + heightmap[r][c]
            print(f"Row: {r}, Col: {c}")

print(risk_sum)

file.close()