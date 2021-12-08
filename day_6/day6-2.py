<<<<<<< HEAD
file = open("day_6_input.txt", "r")
data = file.read().strip().split(",")

crab_levels = [int(x) for x in data]

top_level = min(crab_levels)
bottom_level = max(crab_levels)

move_costs = []

for i in range(top_level, bottom_level + 1):
    level_cost = 0
    for crab in crab_levels:
        n = abs(crab - i)
        level_cost += n*(n+1)/2

    move_costs.append(level_cost)

print(min(move_costs))

=======
from collections import Counter

MATURATION_DAYS = 9
SIM_LEN = 256

# data prep
file = open("day_6_input.txt", "r")
fish_ages = [int(i) for i in file.read().strip().split(",")]

# initialize count values, including those for age with no count
fish_counter = Counter(fish_ages)
for day in range(MATURATION_DAYS):
    if day not in fish_counter.keys():
        fish_counter[day] = 0

# run thru fish generation simulation
for day in range(SIM_LEN):
    count_at_zero = fish_counter[0]
    
    for age in range(1,MATURATION_DAYS):
        fish_counter[age-1] = fish_counter[age]

    fish_counter[6] += count_at_zero
    fish_counter[8] = count_at_zero

print(f"Counter total: {sum(fish_counter.values())}")
>>>>>>> de7baeb91be0205c810c4ae3e86f0f8cef6afe5d
file.close()