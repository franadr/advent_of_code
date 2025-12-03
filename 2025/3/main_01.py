
from collections import OrderedDict, defaultdict
# INPUT = "ex"
INPUT = "all"


def read_input():
    fn = f"input_{INPUT}.txt"
    out = []
    out_2 = []
    with open(fn) as file:
        while line := file.readline():
            bank = defaultdict(list)
            [bank[n].append(i) for i, n in enumerate(list(line.strip()))]
            out.append(OrderedDict(sorted(bank.items())))
            out_2.append([int(n) for n in list(line.strip())])
    return out, out_2


def main():
    dict_input, list_input = read_input()
    res = 0
    for indexes, bank in zip(dict_input, list_input):
        while True:
            max_v, max_indexes = indexes.popitem(last=True)
            max_i = max_indexes[0]
            if max_i < len(bank) - 1:
                next_max = sorted(bank[max_i + 1:])[-1]
                res += int(f"{max_v}{next_max}")
                print(f"{bank} -> {max_v}{next_max}")
                break
    print(res)


main()




