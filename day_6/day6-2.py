from collections import Counter

MATURATION_DAYS = 9
SIM_LEN = 256

file = open("day_6_input.txt", "r")
data = file.read().strip().split(",")

# pairs of start end pairs
fish_ages = [int(i) for i in data]
fish_counter = Counter(fish_ages)

# initialize missing values
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
file.close()