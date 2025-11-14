
# INPUT = "ex"
INPUT = "all"


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
    for i, digit in enumerate(input):
        is_file = i % 2 == 0
        for n in range(0, int(digit)):
            if is_file:
                parsed_input.append(fileid_counter)
                digit_counter += 1
            else:
                parsed_input.append(".")

        fileid_counter += 1 if is_file else 0

    counter = 0
    right_index = len(parsed_input) - 1
    left_index = 0
    while counter < digit_counter - 1:
        current_left = parsed_input[left_index]
        if current_left != '.':
            counter += 1
            left_index += 1
            continue

        current_right = parsed_input[right_index]
        if current_right == '.':
            right_index -= 1
            continue

        parsed_input[left_index] = current_right
        parsed_input[right_index] = '.'
        counter += 1
        right_index -= 1
        left_index += 1

        check_sum = 0
    for i, n in enumerate(parsed_input):
        if n == '.':
            continue
        check_sum += i * n

    print(check_sum)


main()


