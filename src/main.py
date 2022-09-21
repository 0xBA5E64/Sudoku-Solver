from lib import Sudoku, solve_absolutes, reduced_brute
import logging
logging.basicConfig(
    format="[%(asctime)s] %(levelname)s: %(message)s", level=logging.WARNING)


def main():
    my_sudoku = Sudoku([
        0,0,0,2,3,0,1,8,0,
        0,4,0,0,0,0,0,3,0,
        1,0,0,6,0,9,7,0,0,
        0,7,4,8,0,3,0,0,0,
        0,0,0,0,9,0,6,0,0,
        3,0,9,0,0,0,0,7,0,
        2,0,3,5,8,6,0,1,7,
        0,8,0,0,0,0,0,6,2,
        4,6,1,3,7,0,0,5,9,
    ])

    print("00 - Untouched:")
    my_sudoku.print()

    solve_absolutes(my_sudoku)
    print("01 - Absolutes solved:")
    my_sudoku.print()

    reduced_brute(my_sudoku)
    print("02 - Reduced brute-force attack")
    my_sudoku.print()

if __name__ == "__main__":
    main()
