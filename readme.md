# Dovah's `sudoku_solver`
*A small-scale puzzle project* 🔢

⚠️ fair **Warning:** This project was built for novice demonstration purposes only, and is not guaranteed to work at any scale greater than that.

## What is this?
A friend of mine learning Python set out to develop an automatic sudoku solver as a learning project. They planned to go about this by simply brute-forcing every possible combination for the blanks until a solution is found.

### Project Prerequisites:
- The sudoku puzzle is to be provided as an 81-entry long *__one-dimensional__* array of integers, where numbers ranging from 1-9 equal said number in said spot, and a 0 equal an empty slot.
- The solver, be it complete, should be capable of timing itself for comparison against other potential algorithms.

Hearing of this, I proposed a handful of theoretical improvements to such a program:
 - Firstly, cycle through all blank spaces on the board, and check which digits are so far yet free to be used for each blank space.
   - If any of these blank spaces turn out to only have *one* potential digit in it's current state (a so-called "absolute answer" moving forward), add that to the solution, and try again to see if the sudoku board, with these newly filled-in digits, allow for any further "absolute answers".
- Once no further "absolute answers" can be found, iterate over the board, much like a traditional brute-force attack, only with the limited set of potential digits previously calculated in the former step.

This method would theoretically greatly improve the performance of such a program, by eliminating much of what we can already surmise is unneccenary.


## Requirements
 - 🐍 Python 3 (Developed @ 3.10.6)

That's it! No third-party modules or packages.

## Reduced Bruteforce - The Problem:
Once all the "absolute answers" have been put in place, it's time to iterate over the remaining slots.

- The *easy* but slow way of doing this would be to simply count all of the empty slots that remain, (eg; 6), and simply iterate from 0 to 999999, putting each digit in a respective remaining spot on the board, and testing *every* combination. This would *work* since counting upwards from 0 to any number of digits inherently exhausts every possible combination that can be made with said count of digits. However, this would get ridiculously slow, as each empty space would exponentially increase the amount of work needed by a factor of *10*; although we might be able to get away with testing 6 empty spaces, meaning iterating from 0 to 999.999, the current board, post "absolute answering", still has *39* empty spaces, meaning we'd have to iterate from 0 to 999999999999999999999999999999999999999, were we generous and said each test took 1 millisecond, that would still leave us with around 34446649029982363315696649029 years of iteration on our hands, and that, simply won't do.
- The *better* way to do this would be to instead only iterate the digits that are plausible in each blank, meaning if we have a spot we know will only take 2, 5 or 7, there is no need to test it with 1, 3, 4, 6, 8, or 9. If we just keep doing this while iterating through every blank, we should at some point arrive at the last blank with only one fitting digit, we can be sure we've arrived at a valid solution. 