file = open("day_8_input.txt", "r")
data = file.read().strip().split("\n")

  #              0, 1, 2, 3, 4, 5, 6
_num_configs = {(1, 1, 1, 0, 1, 1, 1): 0,   # zero
                (0, 0, 1, 0, 0, 1, 0): 1,
                (1, 0, 1, 1, 1, 0, 1): 2,
                (1, 0, 1, 1, 0, 1, 1): 3,
                (0, 1, 1, 1, 0, 1, 0): 4,
                (1, 1, 0, 1, 0, 1, 1): 5,
                (1, 1, 0, 1, 1, 1, 1): 6,
                (1, 0, 1, 0, 0, 1, 0): 7,
                (1, 1, 1, 1, 1, 1, 1): 8,
                (1, 1, 1, 1, 0, 1, 1): 9}   

# a zero
#    (1)           -      _
#   (1,1)         | |    | |
#    (0)                 |_|
#   (1,1)         | |    
#    (1)           _    
# 
#    (0)           -      _
#   (1,2)         | |    | |
#    (3)                 |_|
#   (4,5)         | |    
#    (6)           _      

def build_solution(scrambled_segments):
    soln_map = {0: "", 1: "", 2: "", 3: "", 4: "", 5: "", 6:""}
    _i_map = {2: [], 3: [], 4: [], 5: [], 6: [], 7: []}

    for _chars in scrambled_segments:
        _i_map[len(_chars)].append(_chars)

    # find position 0
    for c in _i_map[3][0]:
        if c not in _i_map[2][0]:
            soln_map[0] = c
    
    #print(f"Position 0: {soln_map[0]}")

    # find number 6, doesn't have both chars from num one
    num_6_chars = ""
    for seq in _i_map[6]:
        if not (_i_map[2][0][0] in seq and _i_map[2][0][1] in seq):
            num_6_chars = seq

    #print(f"Num 6 is: {num_6_chars}")

    if _i_map[2][0][0] in num_6_chars:
        soln_map[5] = _i_map[2][0][0]
        soln_map[2] = _i_map[2][0][1]
    else:
        soln_map[2] = _i_map[2][0][0]
        soln_map[5] = _i_map[2][0][1]

    # find num 3, only of len 5 that has all of 7's chars
    num_3_chars = ""
    for seq in _i_map[5]:
        if _i_map[3][0][0] in seq and _i_map[3][0][1] in seq and _i_map[3][0][2] in seq:
            num_3_chars = seq

    #print(f"Num 3 is: {num_3_chars}")

    mid_bot_chars = ""
    
    for c in num_3_chars:
        if c not in _i_map[3][0]:
            mid_bot_chars += c

    for seq in _i_map[6]:
        if not (mid_bot_chars[0] in seq and mid_bot_chars[1] in seq):
            # working with a zero
            if mid_bot_chars[0] not in seq:
                soln_map[3] = mid_bot_chars[0]
                soln_map[6] = mid_bot_chars[1]
            else:
                soln_map[6] = mid_bot_chars[0]
                soln_map[3] = mid_bot_chars[1]



    for seq in _i_map[5]:
        if seq != num_3_chars and soln_map[2] in seq:
            # working with num 2
            for c in seq:
                if c not in soln_map.values():
                    soln_map[4] = c
                    break

    for c in _i_map[7][0]:
        if c not in soln_map.values():
            soln_map[1] = c
            break

    
    # print("Solution Map")
    # for i in range(len(soln_map)):
    #     print(i,":", soln_map[i])
    
    real_soln_map = dict()
    
    zero = str(soln_map[0]+soln_map[1]+soln_map[2]+soln_map[4]+soln_map[5]+soln_map[6])
    one = str(soln_map[2]+soln_map[5])
    two = str(soln_map[0]+soln_map[2]+soln_map[3]+soln_map[4]+soln_map[6])
    three = str(soln_map[0]+soln_map[2]+soln_map[3]+soln_map[5]+soln_map[6])
    four = str(soln_map[1]+soln_map[2]+soln_map[3]+soln_map[5])
    five = str(soln_map[0]+soln_map[1]+soln_map[3]+soln_map[5]+soln_map[6])
    six = str(soln_map[0]+soln_map[1]+soln_map[3]+soln_map[4]+soln_map[5]+soln_map[6])
    seven = str(soln_map[0]+soln_map[2]+soln_map[5])
    eight = str(soln_map[0]+soln_map[1]+soln_map[2]+soln_map[3]+soln_map[4]+soln_map[5]+soln_map[6])
    nine = str(soln_map[0]+soln_map[1]+soln_map[2]+soln_map[3]+soln_map[5]+soln_map[6])

    real_soln_map[''.join(sorted(zero))] = 0
    real_soln_map[''.join(sorted(one))] = 1
    real_soln_map[''.join(sorted(two))] = 2
    real_soln_map[''.join(sorted(three))] = 3
    real_soln_map[''.join(sorted(four))] = 4
    real_soln_map[''.join(sorted(five))] = 5
    real_soln_map[''.join(sorted(six))] = 6
    real_soln_map[''.join(sorted(seven))] = 7
    real_soln_map[''.join(sorted(eight))] = 8
    real_soln_map[''.join(sorted(nine))] = 9

    return real_soln_map

count = 0

for line in data:
    left, right = line.strip().split("|")
    right_values = right.strip().split(" ")

    curr_soln = build_solution(left.strip().split(" "))

    curr_val = curr_soln[''.join(sorted(right_values[0]))]*1000 
    curr_val += curr_soln[''.join(sorted(right_values[1]))]*100 
    curr_val += curr_soln[''.join(sorted(right_values[2]))]*10 
    curr_val += curr_soln[''.join(sorted(right_values[3]))]

    print(curr_val)

    count += curr_val

print(count)



file.close()