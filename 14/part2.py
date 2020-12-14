import re


def parse_file(name):
    lines = open(name).read().splitlines()
    instr = []

    for line in lines:
        if line.startswith("mask"):
            mask = re.search("mask = ([X01]+)", line).group(1)
            ormask = int(mask.replace("X", "0"), base=2)

            floats = []
            for pos, char in enumerate(mask):
                if char == 'X':
                    floats.append(len(mask) - pos - 1)

            instr.append(("mask", ormask, floats))
        else:
            address, value = re.search("mem\\[(\\d+)\\] = ([0-9]+)", line).groups()
            instr.append(("set", int(address), int(value)))

    return instr


def setbit(number, bit, value):
    if value == 1:
        return number | (2 ** bit)
    elif value == 0:
        return number & ~(2 ** bit)


def flotations(addr, ormask, floats):
    addr = addr | ormask

    if len(floats) == 0:
        return [addr]

    addresses = []
    for flotation in range(2 ** len(floats)):
        curaddr = addr
        for idx, floater in enumerate(floats):
            curaddr = setbit(curaddr, floater, flotation >> (len(floats) - idx - 1) & 1)
        addresses.append(curaddr)

    return addresses


def run_program(program):
    ormask = 0
    floats = []
    memory = {}

    for idx, instruction in enumerate(program):
        if instruction[0] == "mask":
            _, ormask, floats = instruction
        else:
            _, baseaddress, value = instruction
            for address in flotations(baseaddress, ormask, floats):
                memory[address] = value

    sum = 0
    for n in memory.values():
        sum += n

    return sum


def part2(filename="input"):
    return run_program(parse_file(filename))
