from functools import reduce


def parse_file(name):
    lines = open(name).read().splitlines()
    linescursor = iter(lines)

    rules = []
    for line in linescursor:
        if line == "":
            break

        [name, subrules] = line.split(": ")
        subrules = subrules.split(" or ")
        for idx, subrule in enumerate(subrules):
            subrules[idx] = list(map(lambda s: int(s), subrule.split("-")))
        rules.append(subrules)

    assert(next(linescursor) == "your ticket:")
    myticket = list(map(lambda s: int(s), next(linescursor).split(",")))
    assert(next(linescursor) == "")

    assert(next(linescursor) == "nearby tickets:")

    tickets = []
    for line in linescursor:
        tickets.append(list(map(lambda s: int(s), line.split(","))))

    return rules, myticket, tickets


def try_rules(rules, myticket, tickets):
    invalid_values = []
    for ticket in tickets:
        for field in ticket:
            valid = False
            for rule in rules:
                for left, right in rule:
                    if field in range(left, right + 1):
                        valid = True
            if not valid:
                invalid_values.append(field)

    return reduce(lambda x, acc: x + acc, invalid_values)
