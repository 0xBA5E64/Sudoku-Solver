# Dovah's `sudoku_solver`
*A small scale puzzle project*

⚠️ fair **Warning:** This project was built for novice demonstration purposes only, and is not guaranteed to work at any scale greater than that.

## What is this?
A friend of mine learning Python set out to develop an automatic sudoku solver as a learning project. They planned to go about this by simply brute-forcing every possible combination for the blanks until a solution is found. Hearing of this, I proposed a handful of theoretical improvements to such a program:
 - Firstly, cycle through all blank spaces on the board, and check which digits are so far yet free to be used for each blank space.
   - If any of these blank spaces turn out to only have *one* potential digit in it's current state (a so-called "absolute answer" moving forward), add that to the solution, and try again to see if the sudoku board, with these newly filled-in digits, allow for any further "absolute answers".
- Once no further "absolute answers" can be found, iterate over the board, much like a traditional brute-force attack, only with the limited set of potential digits previously calculated in the former step.

This method should theoretically greatly improve the performance of such a program, by eliminating much of what we can already surmise is unmercenary.

## Project Prerequisites:
- The sudoku puzzle is to be provided as an 81-entry long *__one-dimensional__* array of integers, where numbers ranging from 1-9 equal said number in said spot, and a 0 equal an empty slot.
- The solver, be it complete, should be capable of timing itself for comparison against other potential algorithms.