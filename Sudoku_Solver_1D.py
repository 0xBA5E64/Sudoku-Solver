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
SUDOKU_SUBBOX_SIZE = 3

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

def sudokuGetSqr(input, pos):
    out = []

    # SQuaRe ID
    sqrid = pos // SUDOKU_SUBBOX_SIZE % SUDOKU_SUBBOX_SIZE + (pos // (SUDOKU_SIZE * SUDOKU_SUBBOX_SIZE) * SUDOKU_SUBBOX_SIZE)
    #sqrid = pos // 3 % 3 + (pos // 27 * 3)
    # ^ This needs an expaination.
    #
    #  > i // 3 % 3 + (i // 27 * 3) 
    #
    #          "i // 3" gives you an incrament on threes, 000_111_222_333_444_555 etc.
    #            " % 3" wraps that to be 000_111_222_000_111_222 etc.
    # "+ (i // 27 + 3)" then also increments on 27, which is to say on every 3rd *row*
    #
    # This, in summary, gives, if iterated through with i going from 0-80 in "i // 3 % 3 + (i // 27 * 3)"";
    #
    # [0,0,0,1,1,1,2,2,2,
    #  0,0,0,1,1,1,2,2,2,
    #  0,0,0,1,1,1,2,2,2,
    #  3,3,3,4,4,4,5,5,5,
    #  3,3,3,4,4,4,5,5,5,
    #  3,3,3,4,4,4,5,5,5,
    #  6,6,6,7,7,7,8,8,8,
    #  6,6,6,7,7,7,8,8,8,
    #  6,6,6,7,7,7,8,8,8]
    
    # SQuaRe Start Position (top-left)
    sqrsp = (sqrid * SUDOKU_SUBBOX_SIZE % SUDOKU_SIZE) + (sqrid // SUDOKU_SUBBOX_SIZE * (SUDOKU_SUBBOX_SIZE * SUDOKU_SIZE))
    #sqrsp = (sqrid * 3 % 9) + (sqrid // 3 * 27)
    # sigh... ^ this too.
    # (sqrid  * 3 %  9) gets us to the right column.
    # (sqrid // 3 * 27) gets us to the right row. (every 3rd sqrid we increase the sqrsp by 27)

    for i in range(3):
        out.extend(input[sqrsp+(SUDOKU_SIZE*i):sqrsp+(SUDOKU_SIZE*i)+SUDOKU_SUBBOX_SIZE])
    
    return out

def sudokuGetAllUsedNumbers(input, pos):
    out = []
    out.extend(sudokuGetRow(input, pos))
    out.extend(sudokuGetCol(input, pos))
    out.extend(sudokuGetSqr(input, pos))

    out = list(set(out))

    return out