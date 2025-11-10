# INPUT = "ex"
from collections import defaultdict


INPUT = "all"


def get_matrix(fn: str, split: str = "", int_parse: bool = False) -> list:
    matrix = []
    with open(fn) as file:
        while line := file.readline():
            matrix.append(list(line.strip()))

    return matrix


def search_antenna_around(grid: list) -> dict:
    list_of_nbg = defaultdict(list)
    row, col = 0, 0
    while row < len(grid):
        col = 0
        while col < len(grid[0]):
            if grid[row][col] != ".":
                list_of_nbg[grid[row][col]].append((row, col))
            col += 1
        row += 1

    return list_of_nbg


def calc_slope(position1: tuple[int, int], position2: tuple[int, int]):

    slope = 0
    col_diff = position1[1] - position2[1]
    row_diff = position1[0] - position2[0]

    if col_diff == 0:
        return -99999
    if row_diff == 0:
        return 99999
    if row_diff != 0 and col_diff != 0:
        return col_diff / row_diff
    return slope


def main():
    grid = get_matrix(f"input_{INPUT}.txt")
    row, col = 0, 0
    antennas = search_antenna_around(grid)

    antinode = set()
    while row < len(grid):
        col = 0
        while col < len(grid[0]):
            cell_value = grid[row][col]
            if cell_value != ".":
                if len(antennas[cell_value]) > 1:
                    antinode.add((row, col))
                col += 1
                continue

            for antenna, positions in antennas.items():
                if len(positions) < 2:
                    continue
                slopes = list(map(lambda p: calc_slope((row, col), p), positions))
                slopes.sort()
                prev_value = float("-inf")
                alignement = False
                for s in slopes:
                    if s == prev_value:
                        alignement = True
                        break
                    prev_value = s
                if alignement:
                    antinode.add((row, col))

            col += 1
        row += 1
    print(len(antinode))


main()
