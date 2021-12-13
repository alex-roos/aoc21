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

for line in data:
    if line[:4] == "fold":
        
        print(int(line[-1]))
    elif line != '':
        col, row = [int(x) for x in line.split(',')]
        print(f"Row {row}, Col {col}")

        if col > paper_width:
            paper_width = col
        if row > paper_height:
            paper_height = row

        dot_list.add((row, col))

paper_height += 1
paper_width += 1

fold_location = 655

print(f"Height: {paper_height}, Width: {paper_width}")

#print_paper(dot_list, paper_height, paper_width)

print(f"Num dots: {len(dot_list)}")

# # horizontal fold line
# for _dot in dot_list.copy():
#     if _dot[0] == fold_location:
#         dot_list.remove(_dot)
#     elif _dot[0] > fold_location:
#         dot_list.remove(_dot)
#         dot_list.add((abs(fold_location*2-_dot[0]), _dot[1]))


# # vertical fold line
for _dot in dot_list.copy():
    if _dot[1] == fold_location:
        dot_list.remove(_dot)
    elif _dot[1] > fold_location:
        dot_list.remove(_dot)
        dot_list.add((_dot[0], abs(fold_location*2-_dot[1])))

# print('*'*50)

# print_paper(dot_list, int(paper_height/2), paper_width)

print(f"Num dots: {len(dot_list)}")

file.close()