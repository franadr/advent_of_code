def calc(curr_result: int, next_digit_index: int, target_result: int, digits: list[int]) -> bool:
    if next_digit_index == len(digits):
        return curr_result == target_result

    if curr_result > target_result:
        return False

    int_string = int(f"{curr_result}{digits[next_digit_index]}")

    return calc(curr_result + digits[next_digit_index], next_digit_index + 1, target_result, digits) or calc(curr_result * digits[next_digit_index], next_digit_index + 1, target_result, digits) or calc(int_string, next_digit_index + 1, target_result, digits)


def main():
    input_fn = "input_all.txt"
    equations = []
    total = 0

    with open(input_fn) as f:
        while l := f.readline():
            initial_split = l.split(":")
            result = int(initial_split[0])
            digits = [int(n) for n in initial_split[1].split()]
            equations.append((result, digits))
            res = calc(0, 0, result, digits)
            if res:
                total += result

    print(total)


main()
