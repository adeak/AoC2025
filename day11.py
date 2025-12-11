from collections import Counter, defaultdict


def day11(inp):
    lines = inp.strip().splitlines()
    connections = {}
    for line in lines:
        source, rest = line.split(': ')
        connections[source] = set(rest.split())
    end = 'out'

    # part 1: you -> out
    start = 'you'
    path_counts = Counter({start: 1})  # device -> number of paths there
    while True:
        for device, multiplicity in list(path_counts.items()):
            if device == end:
                continue
            for other_device in connections[device]:
                path_counts[other_device] += multiplicity
            path_counts[device] -= multiplicity

        if sum(1 for key, value in path_counts.items() if value != 0) == 1:
            # only end left, we're done
            break

    result = path_counts[end]

    return result


def day11b(inp):
    lines = inp.strip().splitlines()
    connections = {}
    for line in lines:
        source, rest = line.split(': ')
        connections[source] = set(rest.split())
    end = 'out'

    # part 2: svr -> {dac, fft} -> out
    start = 'svr'
    targets = frozenset({'dac', 'fft'})
    path_counts = defaultdict(Counter)
    path_counts[start][frozenset()] = 1  # device -> {"dac", "fft"} visited -> number of paths
    while True:
        for device, subdict in list(path_counts.items()):
            if device == end:
                continue
            for visited_before_set, multiplicity in subdict.items():
                if device in targets:
                    # amend path information for next step
                    next_visited_before_set = frozenset(visited_before_set | {device})
                else:
                    # just accumulate paths as usual
                    next_visited_before_set = visited_before_set
                for other_device in connections[device]:
                    path_counts[other_device][next_visited_before_set] += multiplicity
                path_counts[device][visited_before_set] -= multiplicity

        if not any(
                device != end
                for device, subdict in path_counts.items()
                for value in subdict.values()
                if value != 0
            ):
            # only end left, we're done
            break

    result = path_counts[end][targets]

    return result


if __name__ == "__main__":
    testinp = open('day11.testinp').read()
    testinp2 = open('day11.testinp2').read()
    print(day11(testinp), day11b(testinp2))
    inp = open('day11.inp').read()
    print(day11(inp), day11b(inp))
