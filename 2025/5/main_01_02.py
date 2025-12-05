import copy
INPUT = "ex"
INPUT = "all"


def read_input():
    fn = f"input_{INPUT}.txt"
    freshs = []
    ingredients = set()
    counter = 0
    with open(fn) as file:
        while line := file.readline():
            if "-" in line:
                left, right = line.strip().split("-")
                left, right = int(left), int(right)
                freshs.append((left, right))
            elif line != '\n':
                counter += 1
                v = int(line.strip())
                for fl, fr in freshs:
                    if v >= fl and v <= fr:
                        ingredients.add(v)

    return set(freshs), ingredients


def main():
    freshs, ingredients = read_input()
    print(f"answer p1: {len(ingredients)}")
    fresh_iter = copy.deepcopy(sorted(freshs))
    left, right = fresh_iter.pop(0)
    ranges = []
    while elem := fresh_iter.pop(0):
        # breakpoint()
        lower, upper = elem
        if lower <= right:
            if upper > right:
                right = upper
        else:
            ranges.append(right - left + 1)
            left, right = lower, upper
        if not fresh_iter:
            ranges.append(right - left + 1)
            break

    print(f"answer p2: {sum(ranges)}")


main()




