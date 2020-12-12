def read_file(name):
    return open(name).read().splitlines()


def parse(lines):
    parsed = list(map(lambda line: int(line), lines))
    parsed.sort(reverse=True)
    return parsed


def differences(result):
    diffs = [result[0]]
    for pos in range(0, len(result) - 1):
        diffs.append(result[pos + 1] - result[pos])
    diffs.append(3)

    return diffs


def path_count(adapters):
    adapters.append(0)
    paths_from = {}
    paths_from[adapters[0]] = 1

    enumerator = enumerate(adapters)
    next(enumerator)
    for adapter_pos, adapter in enumerator:
        paths_from[adapter] = 0
        for i in range(1, 4):
            next_adapter_pos = adapter_pos - i
            next_adapter = adapters[next_adapter_pos]

            if next_adapter_pos < 0 or next_adapter > adapter + 3:
                break

            paths_from[adapter] += paths_from[next_adapter]

    return paths_from[0]


def part2(filename="input"):
    adapters = parse(read_file(filename))

    paths = path_count(adapters)

    print(paths)
