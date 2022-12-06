file = open("day_14_input.txt", "r")
data = file.read().strip().split("\n")

start_string = data[0]
rules = dict()
pairs_dict_template = dict()

# DEBUGGING
# step_answers = []
# step_answers.append("NCNBCHB")
# step_answers.append("NBCCNBBBCBHCB")
# step_answers.append("NBBBCNCCNBBNBNBBCHBHHBCHB")
# step_answers.append("NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB")

for i in range(2, len(data)):
    _pair = data[i][:2]
    rules[_pair] = data[i][-1]

    pairs_dict_template[_pair] = 0

unique_chars = set()
for _key in rules:
    unique_chars.add(_key[0])
    unique_chars.add(_key[1])

unique_chars_final_count_template = dict()
for _c in list(unique_chars):
    unique_chars_final_count_template[_c] = 0

rule_ratio_char_dict = unique_chars_final_count_template.copy()
rules_str = ""
for _p in rules.keys():
    rules_str + _p
    rule_ratio_char_dict[_p[0]] += 1
    rule_ratio_char_dict[_p[1]] += 1

print(f"Rule Char Counts: {rule_ratio_char_dict}")

ltr_counts_dict = dict()

count_pairs_dict = pairs_dict_template.copy()

# DEBUGGING
# step_answers_list = [count_pairs_dict.copy(), count_pairs_dict.copy(), count_pairs_dict.copy(), count_pairs_dict.copy()]

# _idx = 0
# for _ans in step_answers:
#     for _i in range(len(_ans)-1):
#         step_answers_list[_idx][_ans[_i:_i+2]] += 1
#     _idx += 1
    

for _i in range(len(data[0])-1):
    _pair = data[0][_i] + data[0][_i+1]

    count_pairs_dict[_pair] += 1

file.close()

for _i in range(10):
    new_pairs_count = pairs_dict_template.copy()

    for _key in count_pairs_dict:
        # old pair, e.g. 'CH' becomes 'CB' and 'HB' and each get the same counts as previous
        new_pairs_count[_key[0] + rules[_key]] += count_pairs_dict[_key]
        new_pairs_count[rules[_key] + _key[1]] += count_pairs_dict[_key]

    count_pairs_dict = new_pairs_count.copy()

    _chars_count = unique_chars_final_count_template.copy()

    for _key in count_pairs_dict:
        _chars_count[_key[0]] += count_pairs_dict[_key]
        _chars_count[_key[1]] += count_pairs_dict[_key]

    _chars_count[data[0][0]] += 1
    _chars_count[data[0][-1]] += 1

    for _c in _chars_count.keys():
        _chars_count[_c] = _chars_count[_c] / 2
    
    # print(f"Round {_i+1}: {count_pairs_dict}")
    # print(f"Char Count: {_chars_count}\n")

# DEBUGGING
    # if _i < 4:
    #     print(f"SiteAns: {step_answers_list[_i]}")
    #     print()

unique_chars_final_count = unique_chars_final_count_template.copy()

for _key in count_pairs_dict:
    unique_chars_final_count[_key[0]] += count_pairs_dict[_key]
    unique_chars_final_count[_key[1]] += count_pairs_dict[_key]

print(unique_chars_final_count)

unique_chars_final_count[data[0][0]] += 1
unique_chars_final_count[data[0][-1]] += 1

for _c in unique_chars_final_count.keys():
    unique_chars_final_count[_c] = unique_chars_final_count[_c] / 2

diff = max(unique_chars_final_count.values()) - min(unique_chars_final_count.values())

print(diff)