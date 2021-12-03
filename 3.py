""" Advent of Code 2021
    Day 3
"""
import copy
import io
import unittest
from textwrap import dedent


def part1(data):
    # gamma: most significant, epsilon: least significant
    bit_length = len(data[0].rstrip())
    gamma = [0] * bit_length
    epsilon = [0] * bit_length
    sums = [0] * bit_length
    for i in data:
        for n in range(bit_length):
            sums[n] += int(i[n])

    for n in range(bit_length):
        if sums[n] >= len(data) / 2:
            gamma[n] = 1
            epsilon[n] = 0
        else:
            gamma[n] = 0
            epsilon[n] = 1

    gamma = ''.join(str(i) for i in gamma)
    epsilon = ''.join(str(i) for i in epsilon)

    return gamma, int(gamma, 2), epsilon, int(epsilon, 2)


def part2(data):
    # life support rating = ox * co2
    gamma, _, epsilon, _ = part1(data)
    bit_length = len(data[0].rstrip())

    ox_set = copy.copy(data)
    co2_set = copy.copy(data)

    for n in range(bit_length):
        if len(ox_set) > 1:
            ox_set = [v for v in ox_set if v[n] == gamma[n]]
        if len(co2_set) > 1:
            co2_set = [v for v in co2_set if v[n] == epsilon[n]]

        if len(ox_set) == 1 and len(co2_set) == 1:
            break

        gamma, _, _, _ = part1(ox_set)
        _, _, epsilon, _ = part1(co2_set)

    ox = ox_set[0][:bit_length]
    co2 = co2_set[0][:bit_length]
    return ox, int(ox, 2), co2, int(co2, 2)


class Tests(unittest.TestCase):
    sample = dedent('''\
        00100
        11110
        10110
        10111
        10101
        01111
        00111
        11100
        10000
        11001
        00010
        01010
    ''')

    def test_part_1(self):
        """Test part 1 with sample data."""
        data = [i for i in io.StringIO(self.sample)]
        solution = part1(data)

        self.assertEqual(solution, ('10110', 22, '01001', 9))

    def test_part_2(self):
        """Test part 2 with sample data."""
        data = [i for i in io.StringIO(self.sample)]
        solution = part2(data)

        self.assertEqual(solution, ('10111', 23, '01010', 10))


def main():
    """Day 2."""
    data = [i for i in open('data/3.input', 'r')]
    sol = part1(data)
    print(sol, 'Ans:', sol[1] * sol[3])

    sol = part2(data)
    print(sol, 'Ans:', sol[1] * sol[3])


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        unittest.main(argv=sys.argv[:1])
    else:
        main()
