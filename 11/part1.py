def read_file(name):
    return list(map(lambda s: list(s.strip()), open(name).readlines()))


def at(layout, row, col):
    if row < 0 or row >= len(layout):
        return '.'
    if col < 0 or col >= len(layout[0]):
        return '.'

    return layout[row][col]


def occupied_around(layout, row, col):
    around = 0
    for j in range(-1, 2):
        for i in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if at(layout, row + i, col + j) == '#':
                around += 1

    return around


def iterate(layout):
    line = [0] * len(layout[0])
    new_layout = [line[:] for _ in range(len(layout))]

    for row in range(len(layout)):
        for col in range(len(layout[0])):
            position = at(layout, row, col)
            if position == '.':
                new_layout[row][col] = '.'
                continue

            around = occupied_around(layout, row, col)

            if position == 'L':
                if around == 0:
                    new_layout[row][col] = '#'
                else:
                    new_layout[row][col] = 'L'
            elif position == '#':
                if around >= 4:
                    new_layout[row][col] = 'L'
                else:
                    new_layout[row][col] = '#'

    return new_layout


def part1(filename="input"):
    layout = []
    new_layout = read_file(filename)

    while new_layout != layout:
        layout = new_layout
        new_layout = iterate(layout)

    count = 0
    for row in range(len(new_layout)):
        for col in range(len(new_layout[0])):
            if new_layout[row][col] == '#':
                count += 1

    print(count)
