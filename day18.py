#!/usr/bin/env python

from get_input import get_input, line_parser
from collections import defaultdict

def part1(prog):
    prog_1 = prog_runner(prog)
    prev = None
    for sound in prog_1:
        if sound is None and prev != 0:
            return prev
        else:
            prev = sound

def prog_runner(prog, env=None):
    if env is None:
        env = defaultdict(int, {})
    else:
        env = defaultdict(int, env)
    i = 0
    while True:
        func, reg, *vals = prog[i].split()
        if vals:
            try:
                val = int(vals[0])
            except ValueError:
                val = env[vals[0]]

        if func == 'rcv':
            val = None
            while val is None:
                val = yield
            if val != 0:
                env[reg] = val
        elif func == 'snd':
            try:
                yield int(reg)
            except ValueError:
                yield env[reg]
        elif func == 'set':
            env[reg] = val
        elif func == 'add':
            env[reg] += val
        elif func == 'mul':
            env[reg] *= val
        elif func == 'mod':
            env[reg] %= val
        elif func == 'jgz':
            if env[reg] > 0:
                i += val
                continue
        i += 1

def test_prog_runner():
    prog = prog_runner(TEST_LINES, env={'p': 0})
    assert next(prog) == 1
    assert next(prog) == 2
    assert next(prog) == 0
    assert next(prog) == None
    assert prog.send(3) == None
    assert prog.send(4) == None
    assert prog.send(5) == None

    prog1 = prog_runner(TEST_LINES, env={'p': 0})
    prog2 = prog_runner(TEST_LINES, env={'p': 1})
    excepted = (
            ((1, 1), (None, None)),
            ((2, 2), (None, None)),
            ((0, 1), (None, None)),
            ((None, None), (None, None)),
            ((None, None), (None, None)),
            ((None, None), (1, 1)),
            ((None, None), (2, 2)),
            ((None, None), (1, 0)))
    for rx, tx in excepted:
        assert rx[0] == prog1.send(tx[0])
        assert rx[1] == prog2.send(tx[1])

class Program(object):
    def __init__(self, lines, pid):
        self._runner = prog_runner(lines, env={'p': pid})
        self._pid = pid
        self.sent = 0
        self._tx_queue = []
        self.send(None)

    def send(self, *args):
        val = self._runner.send(*args)
        while val is not None:
            self.sent += 1
            self._tx_queue.append(val)
            val = next(self._runner)

    def __next__(self):
        print('Prog {}: {}: {}'.format(self._pid, self._tx_queue[:10], len(self._tx_queue)))
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
    return prog_1.sent

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
    print('Part 1: {}'.format(part1(lines)))
    print('Part 2: {}'.format(part2(lines)))
