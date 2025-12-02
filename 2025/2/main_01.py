
# INPUT = "input_all.txt"
INPUT = "input_ex.txt"


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
    res = 0
    for pairs in input:
        start, end = pairs
        for i in range(int(start), int(end) + 1):
            size = len(str(i))
            if size % 2 != 0:
                continue
            mid = size // 2
            left, right = str(i)[:mid], str(i)[mid:]
            if left == right:
                print(f"{pairs}\nINVALID {i}\n")
                res += i
    print(res)


main()


