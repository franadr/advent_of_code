# 0 -> 1
# #%2 -> [left][right]
# else -> *2024

from collections import Counter


# INPUT = "ex"
INPUT = "all"
BLINKS = 75


def read_input(fn: str) -> list[int]:

    res = []
    with open(fn) as file:
        while line := file.readline():
            res = list(map(lambda s: int(s), line.split()))

    return res


def main():
    input_file = f"input_{INPUT}.txt"
    initial_stones = read_input(input_file)
    stones = Counter(initial_stones)
    for i in range(BLINKS):
        print(f"{i}/{BLINKS}")
        update = Counter()
        for stone, stone_count in stones.items():
            center, rest = divmod(len(str(stone)), 2)
            if stone == 0:
                update[1] += stone_count
                continue

            if rest != 0:
                update[2024 * stone] += stone_count
                continue

            left, right = divmod(stone, 10**center)
            update[left] += stone_count
            update[right] += stone_count
        stones = update

    print(f"{sum(stones.values())}")


if __name__ == "__main__":
    main()
