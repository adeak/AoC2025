def day01(inp):
    dat = inp.splitlines()
    
    pos = 50
    part1 = 0
    for line in dat:
        dir, count = line[0], int(line[1:])
        sign = 1 if dir == 'R' else -1
        pos += sign*count
        pos %= 100
        if pos == 0:
            part1 += 1

    pos = 50
    part2 = 0
    for line in dat:
        dir, count = line[0], int(line[1:])
        sign = 1 if dir == 'R' else -1
        for _ in range(count):
            pos += sign
            pos %= 100
            if pos == 0:
                part2 += 1

    return part1, part2


if __name__ == "__main__":
    testinp = open('day01.testinp').read()
    print(day01(testinp))
    inp = open('day01.inp').read()
    print(day01(inp))
