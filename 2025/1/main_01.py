
INPUT = "input_all.txt"
# INPUT = "input_ex.txt"


def read_input() -> list:
    out = []
    fn = INPUT
    with open(fn) as file:
        while line := file.readline():
            l, r = line[0], line[1:]
            l = 1 if l == 'R' else -1
            out.append((l, int(r)))

    return out


def main():
    input = read_input()
    pos = 50
    res = 0
    for rot, n in input:
        pos = (rot * n) + pos
        pos = pos % 100
        res += 1 if pos == 0 else 0
    print(res)


main()


