def read_file(name):
    return open(name).read().splitlines()


def parse(lines):
    parsed = list(map(lambda line: int(line), lines))
    parsed.sort()
    return parsed


def differences(result):
    diffs = [result[0]]
    for pos in range(0, len(result) - 1):
        diffs.append(result[pos + 1] - result[pos])
    diffs.append(3)

    return diffs


def part1(filename="input"):
    adapters = parse(read_file(filename))

    diffs = differences(adapters)

    ones = len(list(filter(lambda n: n == 1, diffs)))
    threes = len(list(filter(lambda n: n == 3, diffs)))

    print(ones * threes)
