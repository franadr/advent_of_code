
# INPUT = "ex"
INPUT = "all"


def get_matrix(fn: str, split: str = "", int_parse: bool = False) -> list:
    matrix = []
    with open(fn) as file:
        while line := file.readline():
            matrix.append(list(line.strip()))

    return matrix


def search_antenna_around(grid: list) -> dict:
    list_of_nbg = {}
    row, col = 0, 0
    while row < len(grid):
        col = 0
        while col < len(grid[0]):
            if grid[row][col] != '.':
                list_of_nbg[(row, col)] = grid[row][col]
            col += 1
        row += 1

    return list_of_nbg


def main():
    grid = get_matrix(f"input_{INPUT}.txt")
    row, col = 0, 0
    print(f"Total of {len(grid)} x {len(grid[0])} loaded")
    antennas = search_antenna_around(grid)
    print(f"Antennas : {len(antennas)}")

    antinode = set()
    while row < len(grid):
        col = 0
        while col < len(grid[0]):
            for position, antenna in antennas.items():
                if position == (row, col):
                    continue
                position_diff = (position[0] - row, position[1] - col)
                expected_position = (row + 2 * position_diff[0], col + 2 * position_diff[1])
                expected_antenna = antennas.get(expected_position)
                if expected_antenna and expected_antenna == antenna:
                    antinode.add((row, col))
            col += 1
        row += 1
    print(len(antinode))


main()


