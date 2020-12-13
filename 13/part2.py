def read_file(name):
    return open(name).read().splitlines()


def parse_input(lines):
    time = int(lines[0])
    buslines = lines[1].split(',')

    for idx, busline in enumerate(buslines):
        if busline != 'x':
            buslines[idx] = int(busline)

    return time, buslines


def find_earliest_timestamp(start, modulo, offset, busline):
    multiple = 0
    for i in range(busline):
        if (start + modulo * i) % busline == (busline - offset) % busline:
            multiple = i
            break

    return multiple * modulo + start, modulo * busline


def find_earliest_timestamp_all(buslines):
    start = 0
    modulo = 1

    for offset, busline in enumerate(buslines):
        if busline == 'x':
            continue
        start, modulo = find_earliest_timestamp(start, modulo, offset, busline)

    return start


def part2(filename="input"):
    _, buslines = parse_input(read_file(filename))

    print(find_earliest_timestamp_all(buslines))
