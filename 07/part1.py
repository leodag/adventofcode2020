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
        inner_relationship = relationships.setdefault(color, {})
        inner_relationship[container] = amount

to_search = ['shiny gold']
can_contain = set()
while len(to_search) > 0:
    searching = to_search.pop(0)
    for color in relationships.get(searching, []):
        # already processed
        if color not in can_contain:
            can_contain.add(color)
            to_search.append(color)

print(len(can_contain))
