#!/usr/bin/env python3

from get_input import get_input, line_parser

def distribute(memory):
    while True:
        i, biggest = max(enumerate(memory), key=lambda n: (n[1], -n[0]))
        memory[i] = 0
        for j in range(i+1, i+1+biggest):
            memory[j % len(memory)] += 1
        yield tuple(memory)

def part1(nums):
    sequences_seen = set()
    for count, sequence in enumerate(distribute(nums), 1):
        if sequence in sequences_seen:
            return count
        sequences_seen.add(sequence)

def part2(nums):
    first = None
    sequences_seen = set()
    for count, sequence in enumerate(distribute(nums), 1):
        if sequence in sequences_seen:
            if first is not None:
                return count - first
            first = count
            sequences_seen.clear()
        sequences_seen.add(sequence)

if __name__ == '__main__':
    nums = line_parser(get_input(day=6, year=2017), seperator='\t')
    print("Solution part 1: {}".format(part1(nums)))
    print("Solution part 2: {}".format(part2(nums)))
