import re
import sys
from math import prod

from utils import fetch_input, read_input


def distance(this: tuple[int, int, int], other: tuple[int, int, int]):
    x = (this[0] - other[0]) ** 2
    y = (this[1] - other[1]) ** 2
    z = (this[2] - other[2]) ** 2
    return (x + y + z) ** (1 / 2)


def part1(parsed, loops):
    vectors = [tuple([int(x) for x in line.split(",")]) for line in parsed]
    combinations = [
        (this, other) for i, this in enumerate(vectors) for other in vectors[i + 1 :]
    ]
    combinations = sorted(combinations, key=lambda comb: distance(comb[0], comb[1]))
    connected = set()
    circuits = {}
    circuit_index = 0
    for _ in range(loops):
        shortest_node_a, shortest_node_b = combinations.pop(0)

        connected.add((shortest_node_a, shortest_node_b))
        existing_circuits = 0
        circuit_a = None
        circuit_b = None
        inside = False
        for circuit_id, circuit in circuits.items():
            if shortest_node_a in circuit and shortest_node_b in circuit:
                inside = True
                break

            if shortest_node_a in circuit:
                circuit_a = circuit_id
                existing_circuits += 1

            if shortest_node_b in circuit:
                circuit_b = circuit_id
                existing_circuits += 1

        if existing_circuits == 0 and not inside:
            circuits[circuit_index] = {shortest_node_a, shortest_node_b}
            circuit_index += 1

        if existing_circuits == 1:
            if circuit_a is not None:
                circuits[circuit_a].add(shortest_node_b)
            if circuit_b is not None:
                circuits[circuit_b].add(shortest_node_a)

        if existing_circuits == 2 and circuit_a is not None and circuit_b is not None:
            circuits[circuit_index] = circuits[circuit_a].union(circuits[circuit_b])
            circuits.pop(circuit_a)
            circuits.pop(circuit_b)
            circuit_index += 1

    return prod(sorted([len(c) for c in circuits.values()], reverse=True)[:3])


def part2(parsed):
    vectors = [tuple([int(x) for x in line.split(",")]) for line in parsed]
    combinations = [
        (this, other) for i, this in enumerate(vectors) for other in vectors[i + 1 :]
    ]
    combinations = sorted(combinations, key=lambda comb: distance(comb[0], comb[1]))
    connected = set()
    circuits = {}
    circuit_index = 0
    while True:
        shortest_node_a, shortest_node_b = combinations.pop(0)

        connected.add((shortest_node_a, shortest_node_b))
        existing_circuits = 0
        circuit_a = None
        circuit_b = None
        inside = False
        for circuit_id, circuit in circuits.items():
            if shortest_node_a in circuit and shortest_node_b in circuit:
                inside = True
                break

            if shortest_node_a in circuit:
                circuit_a = circuit_id
                existing_circuits += 1

            if shortest_node_b in circuit:
                circuit_b = circuit_id
                existing_circuits += 1

        if existing_circuits == 0 and not inside:
            circuits[circuit_index] = {shortest_node_a, shortest_node_b}
            circuit_index += 1

        if existing_circuits == 1:
            if circuit_a is not None:
                circuits[circuit_a].add(shortest_node_b)
            if circuit_b is not None:
                circuits[circuit_b].add(shortest_node_a)

        if existing_circuits == 2 and circuit_a is not None and circuit_b is not None:
            circuits[circuit_index] = circuits[circuit_a].union(circuits[circuit_b])
            circuits.pop(circuit_a)
            circuits.pop(circuit_b)
            circuit_index += 1

        if len(circuits.keys()) == 1 and len(list(circuits.values())[0]) == len(
            vectors
        ):
            return shortest_node_a[0] * shortest_node_b[0]


if __name__ == "__main__":
    day = int(re.findall(r"\d+", __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ""
        loops = 10 if len(sys.argv) > 1 else 1000
        content = read_input(day, in_file)
        parsed = content.splitlines()
        print(f"Part 1: {part1(parsed, loops)}")
        print(f"Part 2: {part2(parsed)}")
