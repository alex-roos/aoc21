file = open("day_3_input.txt", "r")

data = file.read().strip().split("\n")

def count_bits_in_position(data_list):
    count_curr_zeroes = [0]*len(data_list[0])
    count_curr_ones = [0]*len(data_list[0])
    
    for line in data_list:
        for bit_idx in range(len(line)):
            if line[bit_idx] == '0':
                count_curr_zeroes[bit_idx] += 1
            else:
                count_curr_ones[bit_idx]+=1

    # print(count_curr_ones)
    # print(count_curr_zeroes)

    return [count_curr_zeroes, count_curr_ones]


o_2_forkeeps = data.copy()
co_2_forkeeps = data.copy()

# print(o_2_forkeeps)

temp_list = []

o2_answer = ''

for i in range(len(data[0])):
    # print("**** Position", i)

    if len(o_2_forkeeps) == 1:
        # print("length 1 is", o_2_forkeeps)
        o2_answer = o_2_forkeeps[0]

    else:
        counts = count_bits_in_position(o_2_forkeeps)

        if counts[0][i] > counts[1][i]:
            # keep values with zero in current i position
            for j in range(len(o_2_forkeeps)):
                if o_2_forkeeps[j][i] == '0':
                    # print(o_2_forkeeps[j])
                    temp_list.append(o_2_forkeeps[j])
        else:
            # keep values with 1 in current i position
            for j in range(len(o_2_forkeeps)):
                if o_2_forkeeps[j][i] == '1':
                    # print(o_2_forkeeps[j])
                    temp_list.append(o_2_forkeeps[j])


        o_2_forkeeps = temp_list.copy()
        temp_list = []
        # print(o_2_forkeeps)

        if len(o_2_forkeeps) == 1:
            o2_answer = o_2_forkeeps[0]



print("O2 answer is:", o2_answer)  
co_2_answer = ''

temp_list = []

for i in range(len(data[0])):
    # print("+++++ Position", i)

    if len(co_2_forkeeps) == 1:
        co_2_answer = co_2_forkeeps[0]
    else:
        counts = count_bits_in_position(co_2_forkeeps)

        if counts[0][i] <= counts[1][i]:
            for j in range(len(co_2_forkeeps)):
                if co_2_forkeeps[j][i] == '0':
                    # print(co_2_forkeeps[j])
                    temp_list.append(co_2_forkeeps[j])
        else:
            for j in range(len(co_2_forkeeps)):
                if co_2_forkeeps[j][i] == '1':
                    # print(co_2_forkeeps[j])
                    temp_list.append(co_2_forkeeps[j])

        co_2_forkeeps = temp_list.copy()
        temp_list = []
        # print(co_2_forkeeps)

        if len(co_2_forkeeps) == 1:
            co_2_answer = co_2_forkeeps[0]

            
print("CO2 ans:", co_2_answer)   

o_2 = []
co_2 = []

# for i in range(len(data[0])):
#     if count_zeroes[i] > count_ones[i]:
#         gamma.append(0)
#         epsilon.append(1)
#     else:
#         gamma.append(1)
#         epsilon.append(0)

# print(o_2)
# print(co_2)

# gamma.reverse()
# epsilon.reverse()




gamma_val = 0
epsilon_val = 0

c_val = 0
o_val = 0

# for j in range(len(o_2)):
#     gamma_val += o_2[j] * 2**j
#     epsilon_val += co_2[j] * 2 ** j

co_2_answer_list = []
o2_answer_list = []

for x in range(len(o2_answer)):
    # super janky
    co_2_answer_list.append(int(co_2_answer[-1*(x+1)]))
    o2_answer_list.append(int(o2_answer[-1*(x+1)]))

# print("CO2 ans list:", co_2_answer_list)
# print("O2 ans list", o2_answer_list)

for j in range(len(co_2_answer_list)):
    c_val += co_2_answer_list[j] * 2 **j
    o_val += o2_answer_list[j] * 2 ** j

# print(o_val)
# print(c_val)

print(o_val * c_val)

file.close()