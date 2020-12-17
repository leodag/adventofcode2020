import numpy as np
import scipy.ndimage


def parse_file(name):
    lines = open(name).read().splitlines()

    slice = []
    for line in lines:
        ll = []
        for state in line:
            if state == "#":
                ll.append(True)
            else:
                ll.append(False)
        slice.append(ll)

    return np.array(slice)


def simulate(start_slice, cycles):
    x, y = np.shape(start_slice)

    sx = x + cycles * 2
    sy = y + cycles * 2
    sz = cycles * 2 + 1
    state = np.zeros((sz, sz, sx, sy))
    start = cycles
    filter = np.ones((3, 3, 3, 3))
    filter[1, 1, 1, 1] = 0

    for j in range(0, y):
        for i in range(0, x):
            state[sz // 2, sz // 2, start + i, start + j] = start_slice[i, j]

    for _ in range(0, cycles):
        convolved = scipy.ndimage.convolve(state, filter, output=int)
        state = ((state > 0) & (convolved == 2)) | (convolved == 3)
    return state


def part2(filename="input"):
    start_slice = parse_file(filename)
    return simulate(start_slice, 6).sum()
