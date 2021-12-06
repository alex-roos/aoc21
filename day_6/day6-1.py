MATURATION_DAYS = 9
SIM_LEN = 80

file = open("day_6_input.txt", "r")
data = file.read().strip().split(",")

# pairs of start end pairs
fish_ages = [int(i) for i in data]

print(fish_ages)

count_at_day = [0] * MATURATION_DAYS

for age in fish_ages:
    count_at_day[age] += 1

print(count_at_day)

for day in range(SIM_LEN):
    count_changes = [0] * MATURATION_DAYS

    count_at_zero = count_at_day[0]

    for age in range(1,MATURATION_DAYS):
        count_changes[age-1] = count_at_day[age]

    count_changes[6] += count_at_zero
    count_changes[8] = count_at_zero

    # print(f"****** Day {day}")
    # print(count_changes)

    count_at_day = count_changes.copy()

    
total = 0
for curr in count_at_day:
    total += curr
print(f"Total fish: {total}")
file.close()