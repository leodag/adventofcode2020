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
    hasyes = set()

    for form in group:
        for question in form:
            hasyes.add(question)

    total += len(hasyes)


print(total)
