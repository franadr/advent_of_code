# INPUT = "ex"
INPUT = "all"


def read_input():
    fn = f"input_{INPUT}.txt"
    nodes = []
    with open(fn) as file:
        while line := file.readline():
            l = line.strip()
            x, y = l.split(',')
            nodes.append((int(x), int(y)))
    return nodes


def area(node1: tuple, node2: tuple) -> int:
    area = abs(node1[0] - node2[0] + 1) * abs(node1[1] - node2[1] + 1)
    return area


def main():
    nodes_raw = read_input()
    done = set()
    max_area = 0
    for node1 in nodes_raw:
        for node2 in nodes_raw:
            if node1 == node2:
                continue
            if (node1, node2) in done:
                continue
            current_area = area(node1, node2)
            max_area = max(current_area, max_area)
    print(max_area)


main()




