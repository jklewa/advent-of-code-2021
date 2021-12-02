""" Advent of Code 2021
    Day 2
"""

import io
import unittest
from collections import namedtuple
from textwrap import dedent

Move = namedtuple('Move', 'horizontal depth aim')


class Sub:
    moves = {
        'forward': Move(1, 0, 0),
        'down': Move(0, 1, 1),
        'up': Move(0, -1, -1),
    }

    def __repr__(self):
        return 'Sub({} {} {}) Ans: {}'.format(
            self.horizontal, self.depth, self.aim,
            self.horizontal * self.depth)

    def __init__(self):
        self.horizontal = self.depth = self.aim = 0

    def _parse_command(self, command):
        direction, steps = command.strip().split(' ')
        move = self.moves[direction]
        return move, int(steps)

    def move(self, command):
        """Moves Sub position."""
        move, steps = self._parse_command(command)
        self.horizontal += move.horizontal * steps
        self.depth += move.depth * steps


class SubAim(Sub):
    def move(self, command):
        """Moves Sub position."""
        move, steps = self._parse_command(command)
        self.horizontal += move.horizontal * steps
        self.depth += self.aim * move.horizontal * steps
        self.aim += move.aim * steps


class Tests(unittest.TestCase):
    sample = dedent('''\
        forward 5
        down 5
        forward 8
        up 3
        down 8
        forward 2
    ''')

    def test_part_1(self):
        """Test part 1 with sample data."""
        sub = Sub()
        for command in io.StringIO(self.sample):
            sub.move(command)

        self.assertEqual(str(sub), 'Sub(15 10 0) Ans: 150')

    def test_part_2(self):
        """Test part 2 with sample data."""
        sub = SubAim()
        for command in io.StringIO(self.sample):
            sub.move(command)

        self.assertEqual(str(sub), 'Sub(15 60 10) Ans: 900')


def main():
    """Day 2."""
    commands = open('data/2.input', 'r')
    sub = Sub()
    for command in commands:
        sub.move(command)
    print(sub)

    commands = open('data/2.input', 'r')
    sub = SubAim()
    for command in commands:
        sub.move(command)
    print(sub)


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        unittest.main(argv=sys.argv[:1])
    else:
        main()
