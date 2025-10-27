INIT_MARKER = "^"


def move_up(grid: list[str], position: tuple) -> list[str]:
    row, col = position
    next_row, next_col = (row - 1, col)
    if next_row < 0:
        return grid
    
    grid[row][col] = "X"
     


def main():
    grid = []
    fn = "input_ex.txt"
    row_count = 0
    start_i, start_j = 0, 0
    with open(fn) as file:
        while l := file.readline():
            grid.append(l.strip())
            if INIT_MARKER in l:
                found = False
                col_count = 0
                itt = iter(l)
                while not found:
                    char = next(itt)
                    if char == INIT_MARKER:
                        found = True
                        start_i, start_j = row_count, col_count
                    col_count += 1

            row_count += 1

    print(f"Start location {start_i},{start_j}")


main()
