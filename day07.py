from collections import Counter


def day07(inp):
    rows = inp.strip().splitlines()
    start = rows[0].index('S')

    # keep track of number of parallel-universe beams in each step
    hit_splitters = set()  # (step, position) tuples for part 1
    worlds = Counter({start: 1})  # beam position -> multiplicity items for part 2
    for step, row in enumerate(rows[1:]):
        splitters = {
            index
            for index, char in enumerate(row)
            if char == '^'
        }
        for beam, multiplicity in worlds.copy().items():
            if beam not in splitters:
                # nothing to do, beams go on
                continue
            hit_splitters.add((step, beam))

            # spawn two displaced beam groups for the next step
            worlds[beam - 1] += multiplicity
            worlds[beam + 1] += multiplicity
            del worlds[beam]

    part1 = len(hit_splitters)
    part2 = sum(worlds.values())

    return part1, part2


if __name__ == "__main__":
    testinp = open('day07.testinp').read()
    print(day07(testinp))
    inp = open('day07.inp').read()
    print(day07(inp))
