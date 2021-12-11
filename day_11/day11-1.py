from collections import deque

def get_neighbors(n_curr_octos, _row, _col):
    _neighbors = []

    if _col > 0:
        _neighbors.append((_row, _col-1))
        if _row > 0:
            _neighbors.append((_row-1, _col-1))
        if _row < len(n_curr_octos) - 1:
            _neighbors.append((_row+1, _col-1))
    
    if _col < len(n_curr_octos[0]) - 1:
        _neighbors.append((_row, _col+1))
        if _row > 0:
            _neighbors.append((_row-1, _col+1))
        if _row < len(n_curr_octos) - 1:
            _neighbors.append((_row+1, _col+1))
     
    if _row > 0:
        _neighbors.append((_row - 1, _col))
    
    if _row < len(n_curr_octos) - 1:
        _neighbors.append((_row + 1, _col))

    return _neighbors


def step(curr_octos):
    _count_flashes = 0

    for row in range(len(curr_octos)):
        for col in range(len(curr_octos[0])):
                curr_octos[row][col] += 1

    # to clean code, populate the stack with every element in the array first, then 
    # only the while loop is needed 
    _to_increase = deque()

    for row in range(len(curr_octos)):
        for col in range(len(curr_octos[0])):
            if curr_octos[row][col] > 9:
                curr_octos[row][col] = 0
                _count_flashes += 1
                for _n in get_neighbors(curr_octos, row, col):
                    _to_increase.append(_n)
    
    while len(_to_increase) > 0:
        _next_n = _to_increase.pop()

        if curr_octos[_next_n[0]][_next_n[1]] != 0:
            curr_octos[_next_n[0]][_next_n[1]] += 1

            if curr_octos[_next_n[0]][_next_n[1]] > 9:
                curr_octos[_next_n[0]][_next_n[1]] = 0
                _count_flashes += 1

                for _n in get_neighbors(curr_octos, _next_n[0], _next_n[1]):
                    _to_increase.append(_n)

    return _count_flashes

file = open("day_11_input.txt", "r")
data = file.read().strip().split("\n")

octos = []

for line in data:
    octos.append([int(i) for i in line])

total_flash_count = 0

for _s in range(100):
    total_flash_count += step(octos)

for _r in octos:
    for _c in _r:
        print(_c, end='')
    print()

print(f"Total flashes: {total_flash_count}")

file.close()