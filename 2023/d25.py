import re
import sys

import graphviz
import numpy as np
from utils import fetch_input, read_input


def part1(parsed, in_file):
    # graph = graphviz.Graph()
    # for line in parsed:
    #     node, neighbors = line.split(':')
    #     neighbors = neighbors.split(' ')
    #     for neighbor in neighbors:
    #         if not neighbor: continue
    #         graph.edge(node, neighbor)
    # graph.engine = 'neato'
    # graph.render('graph', view=True)

    # Cut the graph into 2 parts
    # Example: hfx -- pzl, bvb -- cmg, nvd -- jqt
    # Input: fxn -- ptq, fbd -- lzd, kcn -- szl

    ex = [('hfx', 'pzl'), ('bvb', 'cmg'), ('nvd', 'jqt')]
    inp = [('fxn', 'ptq'), ('fbd', 'lzd'), ('kcn', 'szl')]

    edges = {}
    for line in parsed:
        node, neighbors = line.split(':')
        neighbors = neighbors[1:].split(' ')
        for neighbor in neighbors:
            if node not in edges:
                edges[node] = []
            if neighbor not in edges:
                edges[neighbor] = []
            if in_file == 'x1':
                if (node, neighbor) in ex or (neighbor, node) in ex:
                    continue
            if in_file == '':
                if (node, neighbor) in inp or (neighbor, node) in inp:
                    continue
            edges[node].append(neighbor)
            edges[neighbor].append(node)

    all_nodes = set(edges.keys())
    first_nodes = set()

    start = parsed[0].split(':')[0]
    first_nodes.add(start)
    q = [start]
    while q:
        node = q.pop(0)
        for neighbor in edges[node]:
            if neighbor in first_nodes:
                continue
            first_nodes.add(neighbor)
            q.append(neighbor)

    second_nodes = all_nodes - first_nodes
    return len(first_nodes), len(second_nodes), len(first_nodes) * len(second_nodes)

def part2(parsed, in_file):
    pass

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ''
        content = read_input(day, in_file)
        parsed = content.splitlines()
        print(f'Part 1: {part1(parsed, in_file)}')
        print(f'Part 2: {part2(parsed, in_file)}')