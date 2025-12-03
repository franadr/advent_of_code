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

    input: tuple[list[dict[str, list]], list[list]] = read_input()
    indexes_dicts, banks = input
    bank_size = len(banks[0])
    res = 0

    for indexes, bank in zip(indexes_dicts, banks):
        size = 12
        left = 0
        right = bank_size - size
        joltage_value = ""
        while True:
            # if bank[0] == 2:
            # breakpoint()
            search_arr = bank[left:right]
            print(search_arr)
            max_v = sorted(search_arr)[-1]
            max_i = indexes.get(str(max_v)).pop(0)
            while max_i < left:
                max_i = indexes.get(str(max_v)).pop(0)

            joltage_value = f"{joltage_value}{max_v}"
            joltage_value_size = len(joltage_value)
            # print(f"{bank}\n{search_arr}\n{max_v}\n{joltage_value}\n")
            if joltage_value_size == 12:
                break
            left = max_i + 1
            right = bank_size - (size - joltage_value_size) + 1
        print(joltage_value)
        res += int(joltage_value)
    print(res)


main()
