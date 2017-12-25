#!/usr/bin/env python3

from get_input import get_input, line_parser

def build_bridges(spans):
    queue = [(0, tuple())]
    assert len(spans) == len(set(spans))
    while queue:
        end, bridge = queue.pop(0)
        for span in spans:
            if span in bridge:
                continue

            if end in span:
                new_bridge = bridge + (tuple(span), )
                if span[0] == end:
                    new_end = span[1]
                else:
                    new_end = span[0]
                queue.append((new_end, new_bridge))
        if bridge:
            yield bridge 

test = """0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10"""

def test_build_bridges():
    spans = line_parser(test, parse=parse)
    for i, bridge in enumerate(build_bridges(spans), 1):
        assert 0 in bridge[0]
    assert i == 11

def part1(peices):
    strongest_bridge = 0
    for bridge in build_bridges(peices):
        new_sum = sum(a + b for (a, b) in bridge)
        strongest_bridge = max(strongest_bridge, new_sum)
    return strongest_bridge

def part2(peices):
    strongest_bridge = (0, 0)
    for bridge in build_bridges(peices):
        new_sum = sum(a + b for (a, b) in bridge)
        strongest_bridge = max(strongest_bridge, (len(bridge), new_sum))
    return strongest_bridge[1]

def parse(line):
    a, b = line.split('/')
    return (int(a), int(b))

if __name__ == '__main__':
    lines = line_parser(get_input(day=24, year=2017), parse=parse)
    print("Part 1: {}".format(part1(lines)))
    print("Part 2: {}".format(part2(lines)))
