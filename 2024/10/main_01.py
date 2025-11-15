from collections import defaultdict
import enum


class Node:
    position: tuple[int, int]
    up: "Node"
    right: "Node"
    down: "Node"
    left: "Node"


# INPUT = "ex"
INPUT = "all"


def parse_nodes(fn: str) -> tuple[list[list[int]], list[tuple[int, int]]]:

    grid = []
    start_positions = []
    with open(fn) as file:
        while line := file.readline():
            row = list(map(lambda e: int(e), list(line.strip())))
            if not grid:
                grid.append([-1] * (len(row) + 2))
            row.insert(0, -1)
            row.append(-1)
            grid.append(row)
            row_i = len(grid) - 1
            local_starts = [(row_i, col) for col, v in enumerate(row) if v == 0]
            start_positions.extend(local_starts)
        grid.append([-1] * len(row))

    return grid, start_positions


def main():
    fn = f"input_{INPUT}.txt"
    grid, starts = parse_nodes(fn)
    up, right, down, left = (-1, 0), (0, 1), (1, 0), (0, -1)
    trail_heads = defaultdict(set)
    tc = 0
    for s in starts:
        to_visit = [s]
        while to_visit:
            node_row, node_col = to_visit.pop()
            current = grid[node_row][node_col]
            if current == 9:
                trail_heads[s].add((node_row, node_col))
                tc += 1
                continue
            for row, col in [up, down, right, left]:
                try:
                    target = grid[node_row + row][node_col + col]
                    if target != -1 and target - current == 1:
                        to_visit.append((node_row + row, node_col + col))
                except IndexError:
                    breakpoint()

    res = 0
    for k, v in trail_heads.items():
        res += len(v)
    print(tc)


main()
