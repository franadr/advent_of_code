from collections import Counter
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
    visited = []
    for rot, count in input:
        pos_start = pos
        for i in [rot] * count:
            pos += i
            if pos < 0:
                print(f"Hit!\t{pos_start}\t[{rot},{count}]")
                pos = 99

            if pos > 99:
                print(f"Hit!\t{pos_start}\t[{rot},{count}]")
                pos = 0
            visited.append(pos)

    res = Counter(visited).get(0)
    print(res)


main()

