from collections import defaultdict
import math
INPUT = "ex"
INPUT = "all"


def read_input():
    fn = f"input_{INPUT}.txt"
    columns = defaultdict(list)
    with open(fn) as file:
        while line := file.readline():
            l = line.strip()
            for i, v in enumerate(l.split()):
                if v not in ["*", "+"]:
                    v = int(v)
                columns[i].append(v)
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




