import re


def parse_file(name):
    lines = open(name).read().splitlines()
    instr = []

    for line in lines:
        if line.startswith("mask"):
            mask = re.search("mask = ([X01]+)", line).group(1)
            ormask = int(mask.replace("X", "0"), base=2)
            andmask = int(mask.replace("X", "1"), base=2)

            instr.append(("mask", ormask, andmask))
        else:
            address, value = re.search("mem\\[(\\d+)\\] = ([0-9]+)", line).groups()
            instr.append(("set", int(address), int(value)))

    return instr


def run_program(program):
    ormask = 0
    andmask = 0
    memory = {}

    for instruction in program:
        if instruction[0] == "mask":
            _, ormask, andmask = instruction
        else:
            _, address, value = instruction
            memory[address] = value & andmask | ormask

    sum = 0
    for n in memory.values():
        sum += n

    return sum


def part1(filename="input"):
    return run_program(parse_file(filename))
