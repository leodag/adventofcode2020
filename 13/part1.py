from math import ceil


def read_file(name):
    return open(name).read().splitlines()


def parse_input(lines):
    time = int(lines[0])

    buslines = list(map(lambda bline: int(bline), filter(lambda bline: bline != 'x', lines[1].split(','))))

    return time, buslines


def next_times(time, buslines):
    ntimes = []

    for busline in buslines:
        ntimes.append(ceil(time / busline) * busline)

    return ntimes


def best_bus(time, buslines):
    ntimes = next_times(time, buslines)

    index = ntimes.index(min(ntimes))

    return buslines[index], ntimes[index]


def part1(filename="input"):
    time, buslines = parse_input(read_file(filename))

    busline, busarrival = best_bus(time, buslines)

    print(busline * (busarrival - time))
