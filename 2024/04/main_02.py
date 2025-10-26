def count_diag(matrix: list[str]) -> int:
    next_chars_ref = {"M": "S", "S": "M"}

    count = 0
    i, j = 1, 1
    while i < len(matrix)-1:
        j = 1
        while j < len(matrix[0])-1:
            if matrix[i][j] == 'A':
                ul_i, ul_j = i-1, j-1
                ur_i, ur_j = i-1, j+1
                ll_i, ll_j = i+1, j-1
                lr_i, lr_j = i+1, j+1
                if next_chars_ref.get(matrix[ur_i][ur_j], "1") == matrix[ll_i][ll_j]:
                    count += 1
                if next_chars_ref.get(matrix[ul_i][ul_j], "2") == matrix[lr_i][lr_j]:
                    count += 1
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
