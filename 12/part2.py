def read_file(name):
    return open(name).read().splitlines()


def parse_instructions(lines):
    instructions = []
    for line in lines:
        instruction = line[:1]
        amount = int(line[1:])
        instructions.append((instruction, amount))
    return instructions


def move(position, direction, amount):
    posx, posy = position
    if direction == 'N':
        posy -= amount
    elif direction == 'S':
        posy += amount
    elif direction == 'W':
        posx -= amount
    elif direction == 'E':
        posx += amount
    return posx, posy


def navigate(instructions):
    posx, posy = 0, 0
    wayx, wayy = 10, -1

    for instruction, amount in instructions:
        if instruction == 'R':
            for _ in range(amount % 360 // 90):
                wayx, wayy = -wayy, wayx
        elif instruction == 'L':
            for _ in range(amount % 360 // 90):
                wayx, wayy = wayy, -wayx
        elif instruction == 'F':
            for _ in range(amount):
                posx, posy = posx + wayx, posy + wayy
        else:
            wayx, wayy = move((wayx, wayy), instruction, amount)

    return abs(posx) + abs(posy)


def part2(filename="input"):
    lines = read_file(filename)
    instr = parse_instructions(lines)
    print(navigate(instr))
