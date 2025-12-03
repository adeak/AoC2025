def day03(inp, part2=False):
    banks = inp.strip().splitlines()
    num_digits = 12 if part2 else 2

    result = 0
    for bank in banks:
        digits = []
        remaining_bank = bank
        for digit_ind in range(num_digits, 0, -1):
            # look for first digit in first (total - num_digits + 1) candidates
            digits.append(max(remaining_bank[: len(remaining_bank) - digit_ind + 1]))
            # ignore digits before just found local maximum for next digit
            remaining_bank = remaining_bank[remaining_bank.index(digits[-1]) + 1 :]
        result += int(''.join(digits))

    return result


if __name__ == "__main__":
    testinp = open('day03.testinp').read()
    print(day03(testinp), day03(testinp, part2=True))
    inp = open('day03.inp').read()
    print(day03(inp), day03(inp, part2=True))
