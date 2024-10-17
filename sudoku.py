def display(grid):
    hori_line = "--" * len(grid) + "-"
    print(hori_line)
    for row in grid:
        t = "|{}" * len(grid) + "|"
        print(t.format(*row))
        print(hori_line)

def initialize():
    size = int(input("Enter the grid size (e.g., 4 or 9): "))
    sudoku_state = [[" " for _ in range(size)] for _ in range(size)]

    sudoku_state[0][0] = str(1)
    sudoku_state[1][0] = str(2)
    display(sudoku_state)
    return sudoku_state

def get_user_input(size):
    try:
        row = int(input(f"Enter the row (1 to {size}): ")) - 1
        col = int(input(f"Enter the column (1 to {size}): ")) - 1
        num = input(f"Enter the number to place in row {row + 1}, column {col + 1}: ")
        return row, col, num
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return get_user_input(size)

def is_grid_complete(grid):
    for row in grid:
        if " " in row:
            return False
    return True

def start_game(sudoku_state):
    size = len(sudoku_state)
    while not is_grid_complete(sudoku_state):
        display(sudoku_state)
        row, col, num = get_user_input(size)
        

        if sudoku_state[row][col] == " " and num.isdigit() and 1 <= int(num) <= size:
            sudoku_state[row][col] = num
        else:
            print("Invalid move. Try again.")
    
    print("Congratulations! You've completed the grid.")

def sudoku():
    sudoku_state = initialize()
    start_game(sudoku_state)
    print("Game over!")

sudoku()

