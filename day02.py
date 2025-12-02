def day02(inp):
    pairs_raw = inp.split(',')
    pairs = [
        list(map(int, pair.split('-')))
        for pair in pairs_raw
    ]
    ranges = [range(pair[0], pair[1] + 1) for pair in pairs]

    part1 = part2 = 0
    for range_now in ranges:
        for value in range_now:
            s = str(value)
            # start from longest substring to cover both parts in one stroke
            for l in range(len(s)//2, 0, -1):
                if len(s) % l != 0:
                    continue
                pieces = {
                    s[block*l : (block + 1)*l]
                    for block in range(len(s)//l)
                }
                if len(pieces) != 1:
                    continue

                # here we have an ID we're looking for
                part2 += value
                if 2 * l == len(s):
                    part1 += value
                # no need to check this ID further
                break

    return part1, part2


if __name__ == "__main__":
    testinp = open('day02.testinp').read()
    print(day02(testinp))
    inp = open('day02.inp').read()
    print(day02(inp))
