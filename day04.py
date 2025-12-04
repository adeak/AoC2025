from itertools import count


def day04(inp):
    rolls = {
        (i, j)
        for i, line in enumerate(inp.splitlines())
        for j, char in enumerate(line)
        if char == '@'
    }

    deltas = [
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
    ]

    part1 = part2 = 0
    for i in count(1):
        rolls_remove = set()
        for roll in rolls:
            neighb_count = sum(
                1
                for delta in deltas
                if (roll[0] + delta[0], roll[1] + delta[1]) in rolls
            )
            if neighb_count < 4:
                rolls_remove.add(roll)
        if not rolls_remove:
            # game over
            break

        if i == 1:
            part1 = len(rolls_remove)
        part2 += len(rolls_remove)
        rolls -= rolls_remove

    return part1, part2


if __name__ == "__main__":
    testinp = open('day04.testinp').read()
    print(day04(testinp))
    inp = open('day04.inp').read()
    print(day04(inp))
