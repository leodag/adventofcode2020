import sys

lines = list(map(lambda s: s.strip(), sys.stdin.readlines()))


group = []
groups = []

for line in lines:
    if line == '':
        groups.append(group)
        group = []
        continue

    group.append(line)
groups.append(group)

total = 0

for group in groups:
    hasyes = {}
    group_size = 0

    for form in group:
        group_size += 1
        for question in form:
            hasyes[question] = hasyes.setdefault(question, 0) + 1

    for value in hasyes.values():
        if value == group_size:
            total += 1

print(total)
