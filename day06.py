from io import StringIO

import numpy as np


def day06(inp):
    nums_block, ops_block = inp.strip().rsplit('\n', maxsplit=1)
    nums = np.loadtxt(StringIO(nums_block), dtype='uint64')
    ops = ops_block.split()
    adds = np.array(ops) == '+'

    sums = np.add.reduce(nums[:, adds], axis=0)
    products = np.multiply.reduce(nums[:, ~adds], axis=0)
    result = sums.sum().item() + products.sum().item()

    return result


def day06b(inp):
    nums_block, ops_block = inp.strip().rsplit('\n', maxsplit=1)
    digits_all = np.array([list(line) for line in nums_block.splitlines()]).T[::-1, :]
    ops = ops_block.split()[::-1]

    all_operands = []
    operands = []
    for digits in digits_all:
        num_str = ''.join(digits).strip()
        if not num_str:
            # expression over
            all_operands.append(operands)
            operands = []
            continue

        # continue current expression
        num = int(num_str)
        operands.append(num)

    # add last expression
    all_operands.append(operands)

    result = 0
    for op, operands in zip(ops, all_operands):
        if op == '+':
            subresult = sum(operands)
        else:
            subresult = np.prod(operands).item()

        result += subresult

    return result


if __name__ == "__main__":
    testinp = open('day06.testinp').read()
    print(day06(testinp), day06b(testinp))
    inp = open('day06.inp').read()
    print(day06(inp), day06b(inp))
