file = open("day_13_input.txt", "r")
data = file.read().strip().split("\n")

def print_paper(_dots, height, width):
    for row in range(height):
        for col in range(width):
            if (row, col) in _dots:
                print('# ', end='')
            else: 
                print('. ', end='')
        print()

dot_list = set()

paper_width = -1
paper_height = -1

fold_instructions = []

for line in data:
    if line[:4] == "fold":
        _direction, _value = line.split('=')
        fold_instructions.append((_direction[-1], int(_value)))
    elif line != '':
        col, row = [int(x) for x in line.split(',')]
        #print(f"Row {row}, Col {col}")

        if col > paper_width:
            paper_width = col
        if row > paper_height:
            paper_height = row

        dot_list.add((row, col))

paper_height += 1
paper_width += 1

fold_location = 655

print(fold_instructions)
for _fold in fold_instructions:
    print(f"Height: {paper_height}, Width: {paper_width}")
    print(f"Num dots: {len(dot_list)}")

    fold_location = _fold[1]

    if _fold[0] == 'y':
    # # horizontal fold line
        for _dot in dot_list.copy():
            if _dot[0] == fold_location:
                dot_list.remove(_dot)
            elif _dot[0] > fold_location:
                dot_list.remove(_dot)
                _diff = abs(fold_location - _dot[0])
                if _diff <= fold_location:
                    dot_list.add((fold_location - _diff, _dot[1]))

        paper_height = int(paper_height/2)
    else:
        # # vertical fold line
        for _dot in dot_list.copy():
            if _dot[1] == fold_location:#
                dot_list.remove(_dot)
            elif _dot[1] > fold_location:
                dot_list.remove(_dot)
                _diff = abs(fold_location - _dot[1])
                if _diff <= fold_location:
                    dot_list.add((_dot[0], fold_location - _diff))
        paper_width = int(paper_width/2)


# print('*'*50)

print_paper(dot_list, paper_height, paper_width)

print(f"Num dots: {len(dot_list)}")

file.close()