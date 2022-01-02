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

def sudokuPrint(input):
    i = 0
    while i < len(sudoku):
        tmp = ""
        for i2 in range(9):
            tmp += str(sudoku[i]) + ","
            i+=1
        print(tmp)

def sudokuGetUnsolvedSpaces(input):
    out = []
    for i in range(0,len(input)):
        if input[i] == 0:
            out.append(i);
    return out

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

def sudokuGetAllFreeNumbers(input, pos):
    out = list(range(1,10))

    used = sudokuGetAllUsedNumbers(input, pos)

    for i in used:
        try:
            out.remove(i)
        except:
            continue

    return out

print("SUDOKU STEP 00 - RAW:")
sudokuPrint(sudoku)

# SUDOKU SOLVING STEP 01 - ABSOLUTES
# 
# Before bruteforcing, we can *at least* solve the obvious spaces which-
# are sure to only hold one specific number, no matter what.
# In fact, once that's done, we should try once again, to see if these-
# newly solved spots mark any other openings as "absolutes".

sudoku_solve = sudoku # copy of sudoku which will be modified through solving process
solving      = True   # bool to decide if it's worth still looping or not (set to false on each loop by default, changed to True if a solution is found)
loop         = 0      # integer to keep track of which iteration we're so far on.

while solving:
    solving = False # Pre-emptively set solve to false to stop the loop if nothing happens (will be set to True in case this iteration find any solutions)

    loop+=1 # Iterate loop integer for logging purposes
    print("---ENTERING LOOP ",loop," ---")
    unsolved_spaces= sudokuGetUnsolvedSpaces(sudoku_solve) # Get a list ("unsolved_spaces") of the index of all empty ("0"'d) spaces.
    print("[?] Unsolved Spaces: ", unsolved_spaces) # Verbose

    for current_space in unsolved_spaces: # - - - - - - - - - - Iterate through every unsolved space with "current_space"
        current_openings = sudokuGetAllFreeNumbers(sudoku_solve, current_space) # get openings for *this* current space
        if len(current_openings) == 1: # - - - - - - - - - - -  If only a *single* opening can be found, it is absolute, and part of the final solution
            print("[!] Found absolute solution for Space#", current_space, ": ", current_openings[0]) # Verbose
            sudoku_solve[current_space] = current_openings[0] # Add the space's solution to the sudoku solution.
            solving = True # - - - - - - - - - - - - - - - - -  Since we found a solution and in turn changed the sudoku we're solving, set solving to True to iterate once again in case this space leads to another potential absolute solution.
        #else: # Verbose output option (disabled by default)
        #    print("Possible solutions for Space#", current_space, ": ", current_openings)
    
    if solving == False:
        print("[x] No more solutions found... Stopping loop")

    print("---FINISHING LOOP",loop,"---")

print("Finished Sudoku:")
sudokuPrint(sudoku_solve)