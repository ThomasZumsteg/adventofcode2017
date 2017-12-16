#!/usr/bin/env python3

from get_input import get_input, line_parser

def generator(start, factor, mod=2147483647, critera=1, bits=16):
    while True:
        start = start * factor % mod 
        if start % critera == 0:
            yield start % 2 ** bits

def test_generator():
    b_set = [
        430625591,
        1233683848,
        1431495498,
        137874439,
        285222916
    ]

    a_set = [
        1092455,
        1181022009,
        245556042,
        1744312007,
        1352636452
    ]

    for a, a_gen in zip(a_set, generator(65,16807, bits=32)):
        assert a == a_gen

    for b, b_gen in zip(b_set, generator(8921,16807, bits=32)):
        assert a == a_gen

def part1(start_a, start_b, sample=40000000):
    total = 0
    gen_a = generator(start_a, 16807, bits=16)
    gen_b = generator(start_b, 48271, bits=16)
    for i, (a,b) in enumerate(zip(gen_a, gen_b)):
        if i > sample:
            return total
        if a == b:
            total += 1

def test_part1():
    assert part1(65, 8921, sample=5) == 1
    assert part1(65, 8921) == 588

def part2(start_a, start_b, sample=5000000):
    total = 0
    gen_a = generator(start_a,16807,critera=4,bits=16)
    gen_b = generator(start_b,48271,critera=8,bits=16)
    for i, (a,b) in enumerate(zip(gen_a, gen_b)):
        if i > sample:
            return total
        if a == b:
            total += 1

if __name__ == '__main__':
    a, b = line_parser(get_input(day=15, year=2017), parse=lambda line:int(line.split(' ')[-1]))
    print("Part 1: {}".format(part1(a, b)))
    print("Part 2: {}".format(part2(a, b)))
