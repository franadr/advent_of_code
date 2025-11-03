
from collections import deque,defaultdict
import copy

UP, DOWN, LEFT, RIGHT = "^", "v", "<", ">"
POSITION_INC = {UP: (-1, 0), DOWN: (1, 0), LEFT: (0, -1), RIGHT: (0, 1)}
NEXT_SYMBOL = {UP: RIGHT, RIGHT: DOWN, DOWN: LEFT, LEFT: UP}


def move(grid: list[str], position: tuple) -> tuple[list[str], tuple, str]:
    current_row, current_col = position
    next_symbol = grid[current_row][current_col]
    incr_row, incr_col = POSITION_INC[next_symbol]
    next_row, next_col = current_row + incr_row, current_col + incr_col

    # If we fall outside the grid, it means we are done
    if next_row < 0 or next_row > len(grid)-1:
        return (grid, (current_row, current_col), None)
    if next_col < 0 or next_col > len(grid[0])-1:
        return (grid, (current_row, current_col), None)

    next_val = grid[next_row][next_col]
    next_symbol = grid[current_row][current_col]

    # Until the next candidate position is not '#' no more
    while next_val == "#":
        current_symbol = next_symbol
        next_symbol = NEXT_SYMBOL[current_symbol]
        incr_row, incr_col = POSITION_INC[next_symbol]
        next_row, next_col = current_row + incr_row, current_col + incr_col
        next_val = grid[next_row][next_col]

    grid[current_row][current_col] = "X"
    grid[next_row][next_col] = next_symbol
    return (grid, (next_row, next_col), next_val)


def main():
    original_grid = []
    fn = "input_all.txt"
    row_count = 0
    start_i, start_j = 0, 0
    with open(fn) as file:
        while line := file.readline():
            original_grid.append(list(line.strip()))
            if UP in line:
                found = False
                col_count = 0
                itt = iter(line)
                while not found:
                    char = next(itt)
                    if char == UP:
                        found = True
                        start_i, start_j = row_count, col_count
                    col_count += 1

            row_count += 1

    print(f"Start location {start_i},{start_j}")
    cycle = 0
    total = len(original_grid) * len(original_grid[0])
    progress = 0
    for i in range(len(original_grid)):
        for j in range(len(original_grid[0])):
            progress += 1
            print(f"{progress}/{total}")
            process_grid = copy.deepcopy(original_grid)

            # Set that will track position and associated direction
            visited = {((start_i, start_j), process_grid[start_i][start_j])}

            # Make sure to not replace start position char
            if (i, j) != (start_i, start_j):
                process_grid[i][j] = '#'
            prev_row, prev_col = start_i, start_j
            flag = True
            while flag:
                process_grid, (new_row, new_col), current_val = move(process_grid, (prev_row, prev_col))

                # Our condition if going ouside the grid i.e. escaping
                if new_row == prev_row and new_col == prev_col:
                    break
                post_val = ((new_row, new_col), process_grid[new_row][new_col])

                # The condition of a loop, same cell with same direction
                if post_val in visited:
                    cycle += 1
                    break

                # Otherwise just proceed
                visited.add(post_val)
                prev_row, prev_col = new_row, new_col

    print(cycle)


main()
