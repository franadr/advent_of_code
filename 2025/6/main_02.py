from collections import defaultdict
import math
INPUT = "ex"
# INPUT = "all"


def read_input():
    fn = f"input_{INPUT}.txt"
    columns = defaultdict(list)
    digits = {}
    lines = []
    with open(fn) as file:
        while line := file.readline():
            col_count = 1
            line = line.replace('\n', '')
            lines.append(line)
            if line[0] in ['*', '+']:
                j = -1
                while j >= len(line) * -1:
                    i = -1
                    while line[i] == ' ':
                        i -= 1
                        j -= 1
                    j -= 1
                    digits[f'{col_count}'] = abs(i)
                    col_count += 1

    numbers = []
    for l in lines:
        col_position = -1
        col_count = 1
        line_numbers = []
        while col_position >= len(l) * -1:
            col_end_index = col_position - digits[str(col_count)]
            number = []
            while col_position > col_end_index and col_position > len(l) * -1:
                col_position -= 1
                current = l[col_position]

                number.insert(0, current if current != ' ' else '0')
            col_position -= 1
            col_count += 1
            line_numbers.insert(-1, number)
        numbers.append(line_numbers)
    breakpoint()
    for n in numbers:
        print(n)

    return columns


def main():
    cols = read_input()
    res = 0
    for k, col in cols.items():
        ops = col.pop(-1)
        if ops == "+":
            res += sum(col)
        else:
            res += math.prod(col)

    print(res)


main()




