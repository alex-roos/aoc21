file = open("day_6_input.txt", "r")
data = file.read().strip().split(",")

crab_levels = [int(x) for x in data]

top_level = min(crab_levels)
bottom_level = max(crab_levels)

move_costs = []

for i in range(top_level, bottom_level + 1):
    level_cost = 0
    for crab in crab_levels:
        level_cost += abs(crab - i)

    move_costs.append(level_cost)

print(min(move_costs))

file.close()