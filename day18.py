#!/usr/bin/env python3

from get_input import get_input, line_parser
import logging
import sys
from collections import defaultdict

logging.basicConfig(
        stream=sys.stderr,
        level=logging.INFO)

def part1(prog):
    prog_1 = Program(prog, 0)
    prev = None
    while True:
        sound = next(prog_1)
        if sound is None and prev != 0:
            return prev
        else:
            prev = sound

class Program(object):

    def __init__(self, lines, pid):
        self._program = Program._compile(lines)
        self._pid = pid
        self.env = defaultdict(int, {'p': pid})
        self._runner = self._prog_runner(self._program)
        self._func_pointer = 0
        self.sent = 0
        self._tx_queue = []
        self.send(None)

    def _compile(lines):
        program = []
        for line in lines:
            program.append(tuple(line.split()))
        return tuple(program)

    def _prog_runner(self, program):
        while True:
            func, reg, *args = program[self._func_pointer]
            logging.debug("Pid: {}, Pointer: {}, {}[{}] {} env: {}".format(
                self._pid, self._func_pointer, func, reg, args, dict(self.env)))

            if args:
                try:
                    val = int(args[0])
                except ValueError:
                    val = self.env[args[0]]

            if func == 'rcv':
                recv = None
                while recv is None:
                    recv = yield
                if recv != 0:
                    self.env[reg] = recv
            elif func == 'snd':
                try:
                    yield int(reg)
                except ValueError:
                    yield self.env[reg]
            elif func == 'jgz':
                try:
                    reg_val = int(reg)
                except ValueError:
                    reg_val = self.env[reg]
                if reg_val > 0:
                    self._func_pointer += val
                    continue
            elif func == 'set':
                self.env[reg] = val
            elif func == 'add':
                self.env[reg] += val
            elif func == 'mul':
                self.env[reg] *= val
            elif func == 'mod':
                self.env[reg] %= val
            self._func_pointer += 1

    def send(self, *args):
        val = self._runner.send(*args)
        while val is not None:
            self.sent += 1
            self._tx_queue.append(val)
            val = next(self._runner)

    def __next__(self):
        if len(self._tx_queue) > 0:
            return self._tx_queue.pop(0)
        else:
            return None

    @property
    def blocked(self):
        return len(self._tx_queue) <= 0

def part2(lines):
    prog_1, prog_2 = Program(lines, 0), Program(lines, 1)
    while not (prog_1.blocked and prog_2.blocked):
        prog_2.send(next(prog_1))
        prog_1.send(next(prog_2))
    return prog_2.sent

def test_part2():
    assert 3 == part2(TEST_LINES)

TEST_LINES = [l.strip() for l in 
    """snd 1
       snd 2
       snd p
       rcv a
       rcv b
       rcv c
       rcv d""".splitlines()]

if __name__ == '__main__':
    lines = get_input(day=18, year=2017).splitlines()
    # Part 1: 2951
    # Part 2: 7366
    print('Part 1: {}'.format(part1(lines)))
    print('Part 2: {}'.format(part2(lines)))
