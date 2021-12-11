from collections import deque

file = open("day_10_input.txt", "r")
data = file.read().strip().split("\n")

_match = {'[':']', '{':'}', '(':')', '<':'>'}
_error_vals = {')': 3, ']': 57, '}': 1197, '>': 25137}
_miss_vals = {'(': 1, '[': 2, '{': 3, '<': 4}

symbol_stack = deque()

scores = []

for idx, line in enumerate(data):
    is_corrupt = False
    for _char in line:
        if _char in _match:
            symbol_stack.append(_char)
        else:
            top = symbol_stack.pop()
            if _char == _match[top]:
                pass
            else:
                is_corrupt = True
                break
    if not is_corrupt:
        print(symbol_stack)
        _miss_score = 0
        symbol_stack.reverse()
        for s in symbol_stack:
            _miss_score *= 5
            _miss_score += _miss_vals[s]

        scores.append(_miss_score)
        
        print(f"Missing Score is: {_miss_score}.")

    symbol_stack = deque()

scores.sort()
mid_point = int(len(scores)/2)
print(scores[mid_point])

file.close()