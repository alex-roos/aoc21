from collections import Counter

MATURATION_DAYS = 9
SIM_LEN = 80

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
file.close()