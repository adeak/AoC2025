from io import StringIO

import numpy as np


def day09(inp):
    coords = np.loadtxt(StringIO(inp), delimiter=',', dtype=int)  # shape (n, 2)

    areas = abs(coords[:, 0] - coords[:, None, 0] + 1) * abs(coords[:, 1] - coords[:, None, 1] + 1)
    part1 = areas.max()

    part2 = None

    return part1, part2


if __name__ == "__main__":
    testinp = open('day09.testinp').read()
    print(day09(testinp))
    inp = open('day09.inp').read()
    print(day09(inp))
