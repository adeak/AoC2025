import numpy as np


def day12(inp):
    *present_blocks, spec_block = inp.strip().split('\n\n')

    presents = {}
    for block in present_blocks:
        index, rest = block.split(':\n', maxsplit=1)
        index = int(index)
        shape = np.array([list(line) for line in rest.splitlines()]) == '#'
        presents[index] = shape

    # probably don't need a dict
    assert list(presents) == list(range(len(presents)))
    presents = list(presents.values())
    # probably the case, will use later:
    assert all(present.shape == (3, 3) for present in presents)
    # might as well convert
    presents = np.array(presents)
    
    result = 0
    problematics = []
    for spec in spec_block.splitlines():
        shape, counts = spec.split(': ')
        shape = tuple(map(int, shape.split('x')))
        counts = np.fromstring(counts, sep=' ', dtype=int)

        # first dumb check: total free space
        free_space = np.prod(shape)
        needed_space = (counts * presents.sum(axis=(-2, -1))).sum()
        if needed_space > free_space:
            # can't work
            continue

        # second dumb check: whether enough 3x3 blocks for everyone without bounding box overlaps
        blocks = (np.array(shape) // 3).prod()
        if blocks >= counts.sum():
            result += 1
            continue

        # now we only need to handle the problematic cases, if any
        problematics.append(spec)

    if problematics:
        # just kidding, this is only the test case
        print('to be checked by hand:')
        for spec in problematics:
            print(spec)
        return None

    return result


if __name__ == "__main__":
    testinp = open('day12.testinp').read()
    print(day12(testinp))
    inp = open('day12.inp').read()
    print(day12(inp))
