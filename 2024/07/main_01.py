

def calc(curr_result: int, next_digit_index: int, target_result: int, digits: list[int])-> bool:
    if curr_result == target_result:
        return True

    if curr_result > target_result or next_digit_index > len(digits)-1:
        return False

    inter_result = curr_result + digits[next_digit_index]
    res = calc(inter_result, next_digit_index+1, target_result, digits)
    if not res:
        inter_result = curr_result * digits[next_digit_index]
        return calc(inter_result, next_digit_index+1, target_result, digits)
    else:
        return True


def main():
    input_fn = "input_all.txt"
    equations = []

    with open(input_fn) as f:
        while l := f.readline():
            initial_split = l.split(":")
            result = int(initial_split[0])
            digits = [int(n) for n in initial_split[1].split()]
            equations.append((result, digits))

    total = 0
    for result, digits in equations:
        res = calc(0, 0, result, digits)
        if res:
            total += result

    print(total)


main()
