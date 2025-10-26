def count_diag(matrix: list[str]) -> int:
    next_chars_ref = {"X": ["M", "A", "S"], "S": ["A", "M", "X"]}

    row_max, col_max = len(matrix), len(matrix[0])
    for r in matrix:
        print(r)
    directions = [(1, -1), (1, 1), (1, 0), (0, 1)]
    count = 0
    i, j = 0, 0
    while i < row_max:
        j = 0
        while j < col_max:
            if matrix[i][j] in next_chars_ref.keys():
                for diff_row, diff_col in directions:
                    col, row = j+diff_col, i+diff_row
                    next_i = 0
                    next_chars: list[str] = next_chars_ref[matrix[i][j]]
                    while row < row_max and col < col_max and col > 0:
                        if matrix[row][col] != next_chars[next_i]:
                            break
                        next_i += 1
                        if next_i == len(next_chars):
                            count += 1
                            break
                        row += diff_row
                        col += diff_col
            j += 1
        i += 1

    return count


def main():
    # fn = "input.txt"
    fn = "input_all.txt"
    input_matrix = []
    with open(file=fn) as f:
        while line := f.readline():
            input_matrix.append(f'.{line.strip().strip()}.')
    input_matrix.append(["."]*len(input_matrix[0]))
    count = count_diag(input_matrix)
    print(count)


main()
