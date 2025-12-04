import copy
INPUT = "ex"
INPUT = "all"
OVERFILL_CHARR = 'o'


def read_input():
    fn = f"input_{INPUT}.txt"
    out = []
    with open(fn) as file:
        while line := file.readline():
            row = list(line.strip())
            if not out:
                out.append([OVERFILL_CHARR] * (len(row) + 2))

            row.insert(0, OVERFILL_CHARR)
            row.append(OVERFILL_CHARR)
            out.append(row)
        out.append([OVERFILL_CHARR] * (len(row)))
    return out


def print_grid(grid, cell: tuple[int, int] = None):
    grid_copy = copy.deepcopy(grid)
    if cell is not None:
        grid_copy[cell[0]][cell[1]] = "X"
        print("\n")
    for r in range(len(grid)):
        print(f"{''.join(grid_copy[r])}")


def main():
    grid = read_input()
    res = 0
    tmp_res = -1
    single_pass = False
    while tmp_res != 0:
        row, col = 1, 1
        directions = [(-1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1), (1, -1), (-1, 1)]
        tmp_res = 0
        while grid[row][1] != OVERFILL_CHARR:
            col = 1
            while grid[row][col] != OVERFILL_CHARR:
                # print_grid(grid, (row, col))
                roll_count = 0
                if grid[row][col] == '.':
                    col += 1
                    continue
                for dir_row, dir_col in directions:
                    cell = grid[row + dir_row][col + dir_col]
                    if cell not in ['.', OVERFILL_CHARR]:
                        roll_count += 1
                if roll_count < 4:
                    tmp_res += 1
                    grid[row][col] = '.' if not single_pass else grid[row][col]
                col += 1
            row += 1
        res += tmp_res
        if single_pass:
            tmp_res = 0

    print(res)


main()




