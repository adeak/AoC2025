from collections import defaultdict
from io import StringIO

import numpy as np
import scipy as sp


def day08(inp, testinp=False):
    num_connections = 10 if testinp else 1000

    coords = np.loadtxt(StringIO(inp), delimiter=',', dtype=int)
    distances = sp.spatial.distance.pdist(coords)
    # "For each and (where ),where m is the number of original observations.
    # The metric dist(u=X[i], v=X[j]) is computed and stored in entry
    # m * i + j - ((i + 2) * (i + 1)) // 2"
    dist_inds = [None] * distances.size
    for i, j in np.indices((coords.shape[0],) * 2).reshape(2, -1).T:
        if i >= j:
            continue
        dist_inds[coords.shape[0] * i + j - ((i + 2) * (i + 1)) // 2] = (i.item(), j.item())

    sorting_inds = distances.argsort()
    circuits = [{i} for i in range(coords.shape[0])]  # list of sets, a circuit is a set of indices
    for connection_count, dist_index in enumerate(sorting_inds):
        if connection_count == num_connections:
            # part 1 done
            part1 = np.prod(sorted((len(circuit) for circuit in circuits), reverse=True)[:3]).item()

        i, j = dist_inds[dist_index]
        i_circuit = next(circuit for circuit in circuits if i in circuit)
        j_circuit = next(circuit for circuit in circuits if j in circuit)

        if i_circuit is j_circuit:
            # nothing to do, already connected
            continue

        # else merge circuits
        circuits.remove(j_circuit)
        i_circuit.update(j_circuit)

        if len(circuits) == 1:
            # part 2 done
            part2 = coords[i, 0].item() * coords[j, 0].item()
            break

    return part1, part2


if __name__ == "__main__":
    testinp = open('day08.testinp').read()
    print(day08(testinp, testinp=True))
    inp = open('day08.inp').read()
    print(day08(inp))
