#!/usr/bin/env python3

from get_input import get_input, line_parser
from collections import namedtuple, defaultdict
import logging
import re

log = logging.getLogger(__name__)

Program = namedtuple("Program", ['name', 'weight', 'leaves'])

def part1(tree):
    if len(tree) == 1:
        return tree[0].name
    raise ValueError("To many roots: {}".format(tree))

def part2(tree):
    node = tree[0]
    target = None
    while True:
        weights = defaultdict(list)
        for l in node.leaves:
            weights[weight(l)].append(l)
        if len(weights.keys()) == 1:
            if target is None:
                raise ValueError("Tree is balanced")
            w, nodes = list(weights.items())[0]
            return target - len(nodes) * w
        elif len(weights) == 2:
            node = [nodes for nodes in weights.values() if len(nodes) == 1][0][0]
            target = [w for w, nodes in weights.items() if len(nodes) != 1][0]

def weight(program):
    queue = [program]
    total = 0
    while len(queue) > 0:
        item = queue.pop()
        total += item.weight
        queue.extend(item.leaves)
    return total

def test_weight():
    nodes = Program('pbga', 66, [Program('agfd', 12, [])])
    assert weight(nodes) == 78

def build_tree(programs):
    nodes = {name: Program(name=name, weight=weight, leaves=[]) for
             name, (weight, _) in programs.items()}
    roots = nodes.copy()
    for name, (weight, leaves) in programs.items():
        for leaf in leaves:
            nodes[name].leaves.append(nodes[leaf])
            del roots[leaf]
    return list(roots.values())

def test_build_tree():
    tree_dict = {'pbga': (66, ['agfd']), 'agfd': (12, [])}
    assert build_tree({'pbga': (66, [])}) == [Program('pbga', 66, [])]
    assert build_tree(tree_dict) == [Program('pbga', 66, [Program('agfd', 12, [])])]

def parse(lines):
    # pswzpo (88) -> mfbagfq, ncrtwlq, mfoinlm, lrrdrb
    programs = {}
    for line in lines:
        log.debug(line)
        splits = line.split(' -> ')
        name, weight = splits[0].split()
        weight = int(weight.strip('()'))
        leaves = []
        if len(splits) >= 2:
            leaves.extend(splits[1].split(', '))
        programs[name] = (weight, leaves)
    return programs

def test_parse():
    result = parse(open('day7.sample_input').read().splitlines())
    assert result['pbga'][0] == 66
    assert result['pbga'][1] == []
    assert set(result['fwft'][1]) == set('ktlj, cntj, xhth'.split(', '))

if __name__ == '__main__':
    programs = parse(get_input(day=7, year=2017).splitlines())
    tree = build_tree(programs)
    print('Part 1: {}'.format(part1(tree)))
    print('Part 2: {}'.format(part2(tree)))
