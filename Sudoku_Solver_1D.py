sudoku = [
    0,0,0,2,3,0,1,8,0,
    0,4,0,0,0,0,0,3,0,
    1,0,0,6,0,9,7,0,0,
    0,7,4,8,0,3,0,0,0,
    0,0,0,0,9,0,6,0,0,
    3,0,9,0,0,0,0,7,0,
    2,0,3,5,8,6,0,1,7,
    0,8,0,0,0,0,0,6,2,
    4,6,1,3,7,0,0,5,9,
]

SUDOKU_SIZE = 9

# Get the coordz for all unsolved spaces.
unsolved_spaces = []
for i in range(0,SUDOKU_SIZE):
    if sudoku[i] == 0:
        unsolved_spaces.append(i);
#print(unsolved_spaces)

def sudokuGetRow(input, pos):
    # Loop method:
    out = []
    for i in range(SUDOKU_SIZE):
        out.append(input[(pos // SUDOKU_SIZE) * SUDOKU_SIZE + i])
    return out

def sudokuGetCol(input, pos):
    # Loop method:
    out = []
    for i in range(SUDOKU_SIZE):
        out.append(input[(SUDOKU_SIZE * i) + (pos % SUDOKU_SIZE)])
    return out