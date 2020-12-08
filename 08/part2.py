import sys
import copy


def run_program(instructions):
    visited = set()
    acc = 0
    ip = 0

    while ip not in visited and ip < len(instructions):
        visited.add(ip)

        instr, arg = instructions[ip]

        if instr == "nop":
            None
        elif instr == "acc":
            acc += int(arg)
        elif instr == "jmp":
            ip += int(arg) - 1

        ip += 1

    return ip, acc


instructions = list(map(lambda s: s.split(), sys.stdin.readlines()))

jmp_indices = filter(lambda x: instructions[x][0] == 'jmp', range(0, len(instructions)))

for jmp_index in jmp_indices:
    instr = copy.deepcopy(instructions)
    instr[jmp_index][0] = "nop"

    ip, acc = run_program(instr)

    if ip == len(instr):
        print(acc)
        break
