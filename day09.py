from itertools import combinations
from io import StringIO

import numpy as np


def day09(inp):
    coords = np.loadtxt(StringIO(inp), delimiter=',', dtype=int)  # shape (n, 2)

    areas = abs(coords[:, 0] - coords[:, None, 0] + 1) * abs(coords[:, 1] - coords[:, None, 1] + 1)
    part1 = areas.max().item()

    # part 2: check all valid pairs of corners, check no line between points, and that middle is inside

    edges_horiz = []  # (y0, xmin, xmax) triples for lines along x
    edges_vert = []  # (x0, ymin, ymax) triples for lines along y
    for first, second in zip(coords, np.roll(coords, -1, axis=0)):
        if first[0] == second[0]:
            edges_vert.append((first[0], *sorted([first[1], second[1]])))
        elif first[1] == second[1]:
            edges_horiz.append((first[1], *sorted([first[0], second[0]])))

    part2 = 0
    for first, third in combinations(coords, 2):
        dx, dy = third - first
        if dx * dy == 0:
            # we can definitely do better than a line
            continue

        area = (abs(dx) + 1) * (abs(dy) + 1)
        if area < part2:
            # no need to check anything
            continue

        x1, x2 = sorted([first[0], third[0]])
        y1, y2 = sorted([first[1], third[1]])

        # check intersection with horizontal boundary edges
        if rectangle_has_intersection((x1, x2), (y1, y2), edges_horiz):
            continue

        # check intersection with vertical boundary edges
        if rectangle_has_intersection((y1, y2), (x1, x2), edges_vert):
            continue

        # check if midpoint is inside (to avoid catching a rectangular hole)
        midpoint = (first + third) // 2
        if is_point_inside(midpoint, coords):
            # assume the whole rectangle is fine
            if area > part2:
                part2 = area.item()

    return part1, part2


def rectangle_has_intersection(coords_parallel, coords_perp, edges):
    """Check if edges of a rectangle intersect with the outline along an axis.

    If the rectangle is spanned by (x1, y1) and (x2, y2), then
    coords_parallel is sorted([x1, x2]) and coords_perp is
    sorted([y1, y2]) to be tested against `edges=edges_horiz`. If
    coords_parallel is (y1, y2) and coords_perp is (x1, x2) (give or
    take sorting) then this can be run against `edges=edges_vert`. So
    "parallel" and "perp" are relative to the orientation of the edges
    inside `edges`.
    """
    para1, para2 = coords_parallel
    perp1, perp2 = coords_perp
    for level, start, end in edges:
        if not perp1 < level < perp2:
            # no intersection yet
            continue
        if end <= para1 or start >= para2:
            # no intersection yet
            continue
        # here we have an intersection
        return True
    return False


def is_point_inside(point, coords):
    """Check if a given tile is inside the boundary."""
    if (point == coords).all(-1).any():
        # point is part of the boundary coordinates
        return True

    angle = 0
    for first, second in zip(coords, np.roll(coords, -1, axis=0)):
        # pad to xy plane embedded in 3d
        v1 = np.pad((first - point).astype(float), [0, 1])
        v2 = np.pad((second - point).astype(float), [0, 1])
        v1 /= np.linalg.norm(v1)
        v2 /= np.linalg.norm(v2)
        d_angle = np.arccos(np.clip(v1 @ v2, -1, 1))
        sign = np.sign(np.cross(v1, v2)[-1])
        angle += sign * d_angle

    return np.isclose(angle, (2*np.pi, np.pi)).any()


if __name__ == "__main__":
    testinp = open('day09.testinp').read()
    print(day09(testinp))
    inp = open('day09.inp').read()
    print(day09(inp))
