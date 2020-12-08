import sys

instructions = list(map(lambda s: s.split(), sys.stdin.readlines()))

visited = set()
acc = 0
ip = 0

while ip not in visited:
    visited.add(ip)

    instr, arg = instructions[ip]

    if instr == "nop":
        None
    elif instr == "acc":
        acc += int(arg)
    elif instr == "jmp":
        ip += int(arg) - 1

    ip += 1

print(acc)
