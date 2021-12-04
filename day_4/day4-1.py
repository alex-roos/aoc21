def check_for_win(next_board):
    accum = 0
    for row in range(5):
        for col in range(5):
            accum += next_board[row][col]
        if accum == -5:
            return True
        accum = 0
    
    for col in range(5):
        for row in range(5):
            accum += next_board[row][col]
        if accum == -5:
            return True
        accum = 0

    return False

def update_board(next_board, num_called):
    for row in range(len(next_board)):
        for col in range(len(next_board)):
            if next_board[row][col] == num_called:
                next_board[row][col] = -1

    return next_board.copy()

def calc_score(next_board):
    accum = 0

    for row in next_board:
        for item in row:
            if item != -1:
                accum += item

    return accum

file = open("day_4_input_test.txt", "r")

data = file.read().strip().split("\n")

numbers_called = data[0].split(',')
numbers_called = [int(i) for i in numbers_called]
print(numbers_called)

row_counter = 0
board_counter = 0
boards = []

tmp_board = []
for line in data[2:]:
    #print("next line: ", line)

    if len(line) != 0:

        if row_counter < 5:
            tmp_line = line.split(' ')

            while '' in tmp_line:
                tmp_line.remove('')

            tmp_line = [int(i) for i in tmp_line]
            tmp_board.append(tmp_line)
            row_counter += 1
        
        if row_counter == 5:     
            boards.append(tmp_board)

            board_counter += 1

            tmp_board = []

            row_counter = 0

            if line == '\n':
                print("Row Blank")


print(len(boards))
for b in boards:
    print(b)

winner = -1
last_num = -1

for num in numbers_called:
    if winner != -1:
        break

    print(f"Num called: {num}")

    for idx, brd in enumerate(boards):
        boards[idx] = update_board(brd, num)

        if check_for_win(boards[idx]):
            print("We have a winner")
            print(boards[idx])

            winner = idx
            last_num = num

            break




print(f"Winner is board {winner}")            

print(calc_score(boards[winner]) * last_num)



print(boards)
boards.remove(boards[winner])
print(boards)

file.close()