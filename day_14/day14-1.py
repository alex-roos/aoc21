file = open("day_14_input_test.txt", "r")
data = file.read().strip().split("\n")

start_string = data[0]
rules = dict()

for i in range(2, len(data)):
    rules[data[i][:2]] = data[i][-1]

print(rules)

file.close()