# INPUT = "ex"
from collections import Counter


INPUT = "all"
# INPUT = "ex"


def get_input(fn: str, split: str = "", int_parse: bool = False) -> list:
    matrix = []
    with open(fn) as file:
        while line := file.readline():
            matrix.append(list(line.strip()))

    return matrix


def main():
    fn = f"input_{INPUT}.txt"
    input = get_input(fn)
    assert len(input) == 1
    input = input[0]

    fileid_counter = 0
    parsed_input = []
    digit_counter = 0
    file_counter = {}
    for i, digit in enumerate(input):
        is_file = i % 2 == 0
        if is_file:
            file_counter[fileid_counter] = (int(digit), len(parsed_input))
        for n in range(0, int(digit)):
            if is_file:
                parsed_input.append(fileid_counter)
                digit_counter += 1
            else:
                parsed_input.append(".")

        fileid_counter += 1 if is_file else 0

    while len(file_counter) > 0:
        file_id, (size, index) = file_counter.popitem()
        i = 0
        while i < len(parsed_input):
            while parsed_input[i] != ".":
                i += 1
            space_size = 0
            if index < i:
                break
            _i = i
            while parsed_input[_i] == ".":
                space_size += 1
                _i += 1
            file_fits = size <= space_size
            # breakpoint()
            if file_fits:
                parsed_input[i : i + size] = [file_id] * size
                parsed_input[index : index + size] = ["."] * size
                break
            i += 1

    check_sum = 0
    for i, n in enumerate(parsed_input):
        if n == ".":
            continue
        check_sum += i * n

    print(check_sum)


main()
