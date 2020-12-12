directions = ['N', 'E', 'S', 'W']


def read_file(name):
    return open(name).read().splitlines()


def parse_instructions(lines):
    instructions = []
    for line in lines:
        instruction = line[:1]
        amount = int(line[1:])
        instructions.append((instruction, amount))
    return instructions


def turn(current_direction, amount):
    direction_idx = directions.index(current_direction)
    new_direction_idx = (direction_idx + amount // 90) % len(directions)
    return directions[new_direction_idx]


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
    direction = 'E'

    for instruction, amount in instructions:
        if instruction == 'R':
            direction = turn(direction, amount)
        elif instruction == 'L':
            direction = turn(direction, -amount)
        elif instruction == 'F':
            posx, posy = move((posx, posy), direction, amount)
        else:
            posx, posy = move((posx, posy), instruction, amount)

    return abs(posx) + abs(posy)


def part1(filename="input"):
    lines = read_file(filename)
    instr = parse_instructions(lines)
    print(navigate(instr))
