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

def extract_lines_with_key_val(parse_list, keep_val, position):
    rtn_list = []
    for binary_val in parse_list:
        if binary_val[position] == keep_val:
            rtn_list.append(binary_val)
    return rtn_list

# prepare each original list of binary values
o_2_forkeeps = data.copy()
co_2_forkeeps = data.copy()

i = 0
while len(o_2_forkeeps) > 1:
    counts = count_bits_in_position(o_2_forkeeps)
    curr_keep_val = ''
    
    curr_keep_val = '0' if counts[0][i] > counts[1][i] else '1'
    
    o_2_forkeeps = extract_lines_with_key_val(o_2_forkeeps, curr_keep_val, i).copy()
    i += 1

i = 0
while len(co_2_forkeeps) > 1:
    counts = count_bits_in_position(co_2_forkeeps)

    curr_keep_val = '0' if counts[0][i] <= counts[1][i] else '1'

    co_2_forkeeps = extract_lines_with_key_val(co_2_forkeeps, curr_keep_val, i).copy()
    i += 1

# per Sam, convert binary string to decimal...
print(int(co_2_forkeeps[0],2)*int(o_2_forkeeps[0],2))

file.close()