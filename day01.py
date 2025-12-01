def day01(inp):
    dat = inp.splitlines()
    
    pos = 50
    part1 = part2 = 0
    for line in dat:
        dir, count = line[0], int(line[1:])
        sign = 1 if dir == 'R' else -1
        delta = sign * count

        # part 2: number of full rotations + potential partial rotation
        delta_div, delta_rem = divmod(abs(delta), 100)
        part2 += delta_div
        zero_hit_from_partial = (
            (sign < 0 and delta_rem >= pos) or
            (sign > 0 and delta_rem >= 100 - pos)
        )
        # starting from pos=0 would be a false positive here
        if pos and zero_hit_from_partial:
            part2 += 1

        # part 1: only final state matters
        pos += delta
        pos %= 100
        if pos == 0:
            part1 += 1

    return part1, part2


if __name__ == "__main__":
    testinp = open('day01.testinp').read()
    print(day01(testinp))
    inp = open('day01.inp').read()
    print(day01(inp))
