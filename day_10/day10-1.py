from collections import deque

file = open("day_10_input.txt", "r")
data = file.read().strip().split("\n")

_match = {'[':']', '{':'}', '(':')', '<':'>'}
_error_vals = {')': 3, ']': 57, '}': 1197, '>': 25137}

symbol_stack = deque()

_err_score = 0

for idx, line in enumerate(data):
    for _char in line:
        if _char in _match:
            symbol_stack.append(_char)
        else:
            if _char == _match[symbol_stack.pop()]:
                pass
            else:
                print(f"Corrupt on line {idx} due to {_char}.")
                _err_score += _error_vals[_char]
                break

print(f"Error Score: {_err_score}")

file.close()