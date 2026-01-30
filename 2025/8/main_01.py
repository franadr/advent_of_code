from collections import defaultdict
import math
from dataclasses import dataclass
INPUT = "ex"
# INPUT = "all"


@dataclass(order=True, eq=True)
class Node:
    x: int
    y: int
    z: int

    def __hash__(self) -> int:
        return int(f"{self.x}{self.y}{self.z}")


def read_input():
    fn = f"input_{INPUT}.txt"
    nodes = []
    with open(fn) as file:
        while line := file.readline():
            l = line.strip()
            x, y, z = l.split(',')
            nodes.append(Node(int(x), int(y), int(z)))
    return nodes


def line_distance(node1: Node, node2: Node) -> int:
    d_squared = (node1.x - node2.x)**2 + (node1.y - node2.y)**2 + (node1.z - node2.z)**2
    return math.sqrt(d_squared)


def main():
    nodes_raw = read_input()
    circuits = defaultdict(set)

    distance_ref = defaultdict(list)
    done = set()
    for node1 in nodes_raw:
        for node2 in nodes_raw:
            if node1 == node2 or (node1, node2) in done or (node2, node1) in done:
                continue
            distance = line_distance(node1, node2)
            done.add((node1, node2))
            distance_ref[str(distance)].append((node1, node2))

    distance_ref = sorted(distance_ref.items(), key=lambda e: float(e[0]))
    breakpoint()
    circuits = []
    for j in range(10):
        shortest, nodes = distance_ref.pop(0)
        node1, node2 = nodes[0]
        added = False
        if not circuits:
            circuits.append(set([node1, node2]))
            added = True
        for i, c in enumerate(circuits):
            if node1 in c or node2 in c:
                c.add(node1)
                c.add(node2)
                added = True
                break
        if not added:
            circuits.append(set([node1, node2]))
        print(f"[{j}]:{circuits}")

    circuits.sort(key=lambda s: len(s), reverse=True)
    breakpoint()


main()




