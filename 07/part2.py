import sys

lines = list(map(lambda s: s.strip(), sys.stdin.readlines()))

relationships = {}

for line in lines:
    [container, contained] = line.split(" contain ")
    container = container.removesuffix("s").removesuffix(" bag")
    contained = contained.removesuffix(".")

    if contained == "no other bags":
        continue

    contained = contained.split(", ")
    contained = list(map(lambda s: s.removesuffix("s").removesuffix(" bag"), contained))

    for single_contained in contained:
        [amount, color] = single_contained.split(" ", maxsplit=1)
        # inverted from part1
        inner_relationship = relationships.setdefault(container, {})
        inner_relationship[color] = int(amount)

pending_bags = [('shiny gold', 1)]
bags = -1

while len(pending_bags) > 0:
    color, count = pending_bags.pop(0)
    bags += count
    for inner_color, inner_count in relationships.get(color, {}).items():
        pending_bags.append((inner_color, inner_count * count))

print(bags)
