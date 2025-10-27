UP, DOWN, LEFT, RIGHT = "^", "v", "<", ">"
POSITION_INC = {UP: (-1, 0), DOWN: (1, 0), LEFT: (0, -1), RIGHT: (0, 1)}
ROT_NEXT_POSITION = {UP: RIGHT, RIGHT: DOWN, DOWN: LEFT, LEFT: UP}


def move(grid: list[str], position: tuple) -> tuple[list[str], tuple]:
    row, col = position
    next_row, next_col = POSITION_INC[grid[row][col]]
    new_row, new_col = row + next_row, col + next_col
    if new_row < 0 or new_row > len(grid)-1:
        return (grid, (row, col))
    if new_col < 0 or new_col > len(grid[0])-1:
        return (grid, (row, col))

    new_val = grid[new_row][new_col]
    rot_position = grid[row][col]
    while new_val == "#":
        rot_position = ROT_NEXT_POSITION[grid[row][col]]
        next_row, next_col = POSITION_INC[rot_position]
        new_row, new_col = row + next_row, col + next_col
        new_val = grid[new_row][new_col]

    grid[row][col] = "X"
    grid[new_row][new_col] = rot_position
    return (grid, (new_row, new_col))


def main():
    grid = []
    fn = "input_all.txt"
    row_count = 0
    start_i, start_j = 0, 0
    with open(fn) as file:
        while line := file.readline():
            grid.append(list(line.strip()))
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
    prev_row, prev_col = start_i, start_j
    flag = True
    while flag:
        grid, (new_row, new_col) = move(grid, (prev_row, prev_col))
        print(f"Next post[{new_row}][{new_col}]")
        if new_row == prev_row and new_col == prev_col:
            flag = False
        else:
            prev_row, prev_col = new_row, new_col

    count = 0
    for r in grid:
        for c in r:
            if c == 'X':
                count += 1

    print(count)


main()
