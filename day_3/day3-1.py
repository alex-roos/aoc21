file = open("day_3_input.txt", "r")

data = file.read().strip().split("\n")

count_zeroes = [0]*len(data[0])
count_ones = [0]*len(data[0])
   
for line in data:
    for bit_idx in range(len(line)):
        if line[bit_idx] == '0':
            count_zeroes[bit_idx] += 1
        else:
            count_ones[bit_idx]+=1

print(count_ones)
print(count_zeroes)

gamma = []
epsilon = []

for i in range(len(data[0])):
    if count_zeroes[i] > count_ones[i]:
        gamma.append(0)
        epsilon.append(1)
    else:
        gamma.append(1)
        epsilon.append(0)

print(gamma)
print(epsilon)

gamma.reverse()
epsilon.reverse()

gamma_val = 0
epsilon_val = 0

for j in range(len(gamma)):
    gamma_val += gamma[j] * 2**j
    epsilon_val += epsilon[j] * 2 ** j

print(epsilon_val)
print(gamma_val)

print(epsilon_val*gamma_val)

file.close()