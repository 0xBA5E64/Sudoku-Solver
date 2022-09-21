import logging

class Sudoku:
    """Stores a sudoku board.
    Defaults asks for 81 integers in a list for a traditional 9x9 grid with a sub-grid size of 3x3"""
    def __init__(self: list[int], data, SIZE=9, SUB_SIZE=3):
        self.data = data
        self.SIZE = SIZE
        self.SUB_SIZE = SUB_SIZE
    
    def print(self):
        """ Prints a sudoku-array into a readable block in the user's terminal """
        print( "┌─" + ( "─" * ( self.SIZE *2 ) ) + "┐" ) # Box-drawing top
        for ih in range(self.SIZE): # Iterate through rows
            line = ""
            for iw in range(self.SIZE): # Iterate over entries on line
                line += f"{self.data[ ( ih * self.SIZE) + iw]} "
            print(f"│ {line}│") # Print formatted line with flanking box-drawing characters
        print( "└─" + ( "─" * ( self.SIZE*2 ) ) + "┘" ) # Box-drawing bottom

    def get_unsolved_spaces(self):
        """Returns a list of all indexes for all so far unsolved spacaes"""
        out = []
        for i in range(0,len(self.data)):
            if self.data[i] == 0:
                out.append(i);
        return out
    
    def get_row_of(self, pos: int):
        """Returns a list of all other numbers used on the same row of of the provided index's space"""
        out = []
        for i in range(self.SIZE):
            out.append(self.data[(pos // self.SIZE) * self.SIZE + i])
        return out
    
    def get_col_of(self, pos: int):
        """Returns a list of all other numbers used on the same column of of the provided index's space"""
        out = []
        for i in range(self.SIZE):
            out.append(self.data[(self.SIZE * i) + (pos % self.SIZE)])
        return out
    
    def get_sqr_of(self, pos: int):
        """Returns a list of all other numbers used on the same sub-square of the provided index's space"""
        out = []
    
        # SQuaRe ID
        sqrid = pos // self.SUB_SIZE % self.SUB_SIZE + (pos // (self.SIZE * self.SUB_SIZE) * self.SUB_SIZE)
        #sqrid = pos // 3 % 3 + (pos // 27 * 3)
        # ^ This needs an explanation.
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
        sqrsp = (sqrid * self.SUB_SIZE % self.SIZE) + (sqrid // self.SUB_SIZE * (self.SUB_SIZE * self.SIZE))
        #sqrsp = (sqrid * 3 % 9) + (sqrid // 3 * 27)
        # sigh... ^ this too.
        # (sqrid  * 3 %  9) gets us to the right column.
        # (sqrid // 3 * 27) gets us to the right row. (every 3rd sqrid we increase the sqrsp by 27)
    
        for i in range(3):
            out.extend(self.data[sqrsp+(self.SIZE*i):sqrsp+(self.SIZE*i)+self.SUB_SIZE])
        
        return out
    
    def get_used_of(self, pos: int):
        """Returns a list of all numbers that are already taken for said index's space"""
        out = []
        out.extend(self.get_row_of(pos))
        out.extend(self.get_col_of(pos))
        out.extend(self.get_sqr_of(pos))

        out = list(set(out))

        return out
    
    def get_free_of(self, pos: int):
        """Returns a list of all numbers that are currently free for said index's space"""
        out = list(range(1,10))

        used = self.get_used_of(pos)
        for i in used:
            try:
                out.remove(i)
            except:
                continue

        return out
    
    def check_solved(self):
        """Checks if the current sudoku is verifyably or not"""
        for i in range( len(self.data) ):
            if sorted(self.get_row_of(i)) != list(range(1, self.SIZE+1)):
                return False
            if sorted(self.get_col_of(i)) != list(range(1, self.SIZE+1)):
                return False
            if sorted(self.get_sqr_of(i)) != list(range(1, self.SIZE+1)):
                return False
        return True

def solve_absolutes(input: Sudoku):
    """Partial solver that aims to eliminate obvious answers from a sudoku first.
    This function will iterate and check the options for every blank from the input sudoku.
    If only one option is found for any said spot, said option is applied to the board.
    This process is repeated until all blanks have at least two or more options."""

    solving = True
    loop = 0

    while solving:
        solving = False # Pre-emptively set solve to false to stop the loop if nothing happens (will be set to True in case this iteration find any solutions)
        loop += 1 # Iterate loop integer for logging purposes
        
        logging.info("┌─ ENTERING LOOP %s ---", loop)
        unsolved_spaces = input.get_unsolved_spaces() # Get a list ("unsolved_spaces") of the index of all empty ("0"'d) spaces.
        logging.info("│ [?] Unsolved Spaces (%s): %s", len(unsolved_spaces), unsolved_spaces) # Verbose

        for current_space in unsolved_spaces: # - - - - - - - - - - Iterate through every unsolved space with "current_space"
            current_openings = input.get_free_of(current_space) # get openings for *this* current space
            if len(current_openings) == 1: # - - - - - - - - - - -  If only a *single* opening can be found, it is absolute, and part of the final solution
                logging.info("│ [!] Found absolute solution for Space Nr%s: %s", current_space, current_openings[0]) # Verbose
                input.data[current_space] = current_openings[0] # Add the space's solution to the sudoku solution.
                solving = True # - - - - - - - - - - - - - - - - -  Since we found a solution and in turn changed the sudoku we're solving, set solving to True to iterate once again in case this space leads to another potential absolute solution.
            else: # Verbose output option
                logging.info("│ [?] Possible options for Space Nr%s: %s", current_space, current_openings)

        if solving == False:
            logging.info("│ [x] No more solutions found... Stopping loop")

        logging.info("└─ FINISHING LOOP %s ---\n", loop)

def reduced_brute(input: Sudoku):
    """Solve sudoku through "Reduced/Intelligent Brute-Force Attack" / Recursive Backtracking.
    This function will check and recursively iterate over each possible combination of valid options for the blanks until all have been filled.
    This solver should always return a valid answer to a possible sudoku given enough time."""

    unsolved_spaces = input.get_unsolved_spaces()

    def brute_layer(input, layer=0):
        if layer == len(unsolved_spaces):
            return True
        openings = input.get_free_of(unsolved_spaces[layer])
        for option in openings:
            input.data[unsolved_spaces[layer]] = option
            if brute_layer(input, layer+1):
                return True
        input.data[unsolved_spaces[layer]] = 0
        return False
    
    brute_layer(input)