file = open("day_3_input.txt", "r")

data = file.read().strip().split("\n")

# returns 2d list, first index is list of counts of zeroes for each position
# second index is list of counts of ones for each position
def count_bits_in_position(data_list):
    count_curr_zeroes = [0]*len(data_list[0])
    count_curr_ones = [0]*len(data_list[0])
    
    for line in data_list:
        for bit_idx in range(len(line)):
            if line[bit_idx] == '0':
                count_curr_zeroes[bit_idx] += 1
            else:
                count_curr_ones[bit_idx]+=1

    return [count_curr_zeroes, count_curr_ones]

# prepare each original list of binary values
o_2_forkeeps = data.copy()
co_2_forkeeps = data.copy()

temp_list = []
o2_answer = ''

for i in range(len(data[0])):
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

        if len(o_2_forkeeps) == 1:
            o2_answer = o_2_forkeeps[0]

print("O2 answer is:", o2_answer)  
co_2_answer = ''

temp_list = []

for i in range(len(data[0])):
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

# per Sam, convert binary string to decimal...
print(int(co_2_answer,2)*int(o2_answer,2))

file.close()