
INPUT = "input_all.txt"
# INPUT = "input_ex.txt"


def read_input() -> list:
    out = []
    fn = INPUT
    with open(fn) as file:
        line = file.readline()
        groups = line.split(",")
        out = [[sub.strip() for sub in g.split("-")] for g in groups]

    return out


def main():
    input = read_input()
    res = set()
    for pairs in input:
        start, end = pairs
        for i in range(int(start), int(end) + 1):
            size = len(str(i))
            mid = size // 2
            for power in range(size, mid - 1, -1):
                pattern = i // 10**(power)
                pattern_count = str(i).count(str(pattern))
                if pattern_count * len(str(pattern)) == size and size > 1:
                    res.add(i)
                    print(f"{pairs}:\nINVALID -> {i}(pattern {pattern})\n")
                    break
    print(sum(res))


main()


