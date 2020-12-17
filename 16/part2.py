import numpy as np


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
        rules.append([name, subrules])

    assert(next(linescursor) == "your ticket:")
    myticket = list(map(lambda s: int(s), next(linescursor).split(",")))
    assert(next(linescursor) == "")

    assert(next(linescursor) == "nearby tickets:")

    tickets = []
    for line in linescursor:
        tickets.append(list(map(lambda s: int(s), line.split(","))))

    return rules, myticket, np.array(tickets)


def valid_tickets(rules, tickets):
    valid_tickets = []
    for ticket in tickets:
        ticket_valid = True
        for field in ticket:
            field_valid = False
            for rule in rules:
                for left, right in rule[1]:
                    if field in range(left, right + 1):
                        field_valid = True

            if not field_valid:
                ticket_valid = False

        if ticket_valid:
            valid_tickets.append(ticket)

    return valid_tickets


# This is blasphemous. I tried to make it better but it's still terrible code.
# If you're trying to read this, I'm sorry. I just wanted to make it fast.
# And it's pretty damn slow too.
def categorize(rules, tickets):
    valids = np.array(valid_tickets(rules, tickets))

    validity = []
    names = []
    mappings = {}
    original_indices = list(range(0, len(tickets[0])))

    for name, subrules in rules:
        valid = np.zeros(np.shape(valids), dtype=bool)
        for left, right in subrules:
            valid = valid | ((valids >= left) & (valids <= right))
        names.append(name)
        validity.append(valid)

    validity = np.array(validity)

    for i in range(0, len(validity)):
        columns_that_satisfy_by_rule = validity.all(axis=1)
        columns_that_satisfy = list(columns_that_satisfy_by_rule.sum(axis=1))
        rule_index = columns_that_satisfy.index(1)
        column_index = list(validity[rule_index].all(axis=0)).index(True)

        print("a", rule_index, column_index)

        mappings[original_indices[column_index]] = names[rule_index]
        print(names[rule_index])
        validity = np.delete(validity, rule_index, 0)
        validity = np.delete(validity, column_index, 2)
        original_indices.pop(column_index)
        names.pop(rule_index)

    return mappings


def solve(mappings, myticket):
    prod = 1
    for column_index, column_name in mappings.items():
        if column_name.startswith("departure"):
            prod *= myticket[column_index]

    return prod
