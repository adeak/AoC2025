def day05(inp):
    blocks = inp.strip().split('\n\n')
    fresh_bounds = sorted(
        list(map(int, line.split('-')))
        for line in blocks[0].splitlines()
    )
    availables = list(map(int, blocks[1].splitlines()))

    part1 = sum(
        1
        for available in availables
        if any(
            bounds[0] <= available <= bounds[1]
            for bounds in fresh_bounds
        )
    )

    # bounds are already sorted by start ID, only handle overlaps
    intervals = [fresh_bounds[0]]  # eventually contains final intervals
    for bounds in fresh_bounds[1:]:
        start, end = intervals[-1]
        new_start, new_end = bounds
        if new_end <= end:
            # previous interval already contains current one
            continue
        elif new_start <= end:
            # extend previous interval
            intervals[-1][-1] = new_end
        else:
            # start a new interval
            intervals.append(bounds)

    part2 = sum(interval[1] - interval[0] + 1 for interval in intervals)

    return part1, part2


if __name__ == "__main__":
    testinp = open('day05.testinp').read()
    print(day05(testinp))
    inp = open('day05.inp').read()
    print(day05(inp))
