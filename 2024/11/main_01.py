# 0 -> 1
# #%2 -> [left][right]
# else -> *2024


# INPUT = "ex"
INPUT = "all"
BLINKS = 25


def read_input(fn: str) -> list[int]:

    res = []
    with open(fn) as file:
        while line := file.readline():
            res = list(map(lambda s: int(s), line.split()))

    return res


def apply_rule3(stone_index: int, stone_list: list) -> list:
    stone = stone_list[stone_index]
    stone_list[stone_index] = stone * 2024
    return stone_list


def apply_rule2(stone_index: int, stone_list: list) -> list:
    # split if len(digit) even
    stone = stone_list[stone_index]
    digits = list(str(stone))
    size = len(digits)
    if size % 2 != 0:
        return None

    left = digits[0:size // 2]
    right = digits[size // 2:]
    left_digit = int(''.join(left))
    right_digit = int(''.join(right))
    stone_list[stone_index] = left_digit
    stone_list.insert(stone_index + 1, right_digit)
    return stone_list


def apply_rule1(stone_index: int, stone_list: list) -> list:
    # 0 -> 1
    stone = stone_list[stone_index]
    if stone != 0:
        return None
    stone_list[stone_index] = 1

    return stone_list


def main():
    input_file = f"input_{INPUT}.txt"
    initial_stones = read_input(input_file)
    blink_counter = 0
    stone_list = initial_stones
    for i in range(BLINKS):
        index = 0
        # print(f"[{i}] {stone_list}")
        while index < len(stone_list):
            sl = apply_rule1(index, stone_list=stone_list)
            if sl:
                index += 1
                stone_list = sl
                continue
            sl = apply_rule2(index, stone_list=stone_list)
            if sl:
                index += 2
                stone_list = sl
                continue
            sl = apply_rule3(index, stone_list=stone_list)
            if sl:
                index += 1
                stone_list = sl
                continue
    print(f"{len(stone_list)}")


if __name__ == "__main__":
    main()
