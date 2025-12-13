from ast import literal_eval
from itertools import combinations

import numpy as np
from scipy.optimize import linprog


def day10(inp):
    lines = inp.strip().splitlines()

    part1 = part2 = 0
    for i, line in enumerate(lines):
        lights, rest = line.split(' ', maxsplit=1)
        rest, joltages = rest.rsplit(' ', maxsplit=1)
        buttons = rest.split()

        # convert strings
        lights = [light == '#' for light in lights[1:-1]]  # mask of lights to be on
        joltages = literal_eval(f'[{joltages[1:-1]}]')  # list of int joltages
        buttons = [literal_eval(button) for button in buttons]
        buttons = [button if isinstance(button, tuple) else (button,) for button in buttons]

        # part 1: brute force...
        #         but it only makes sense to press each button 0 or 1 times (2 is a no-op)
        for num_presses in range(1, len(buttons) + 1):
            for button_indices in combinations(range(len(buttons)), num_presses):
                buttons_now = [buttons[index] for index in button_indices]
                pattern = [False] * len(lights)
                for button in buttons_now:
                    for pixel_index in button:
                        pattern[pixel_index] ^= True
                if pattern == lights:
                    # we're good
                    part1 += num_presses
                    break
            else:
                # need more button presses
                continue

            # we got a correct pattern
            break

        # part 2: linear programming...
        #
        # minimize n_1 + n_2 + ... + n_m (for m buttons) such that
        # n_1*b_1^1 + n_2*b_2^1 + ... + n_m*b_n^1 = j^1 where b_c^d indicates if joltage d is in button c
        # ...
        # n_1*b_1^k + n_2*b_2^k + ... + n_m*b_n^k = j^k for k joltages
        c = np.ones(len(buttons), dtype=int)
        b_eq = np.array(joltages)
        A_eq = np.zeros((b_eq.size, c.size), dtype=int)
        for button_index, button in enumerate(buttons):
            A_eq[list(button), button_index] = 1
        res = linprog(c, A_eq=A_eq, b_eq=b_eq, integrality=1)
        assert res.success

        part2 += int(res.x.sum().round())

    return part1, part2


if __name__ == "__main__":
    testinp = open('day10.testinp').read()
    print(day10(testinp))
    inp = open('day10.inp').read()
    print(day10(inp))
