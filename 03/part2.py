import sys

mymap = list(map(lambda s: s.strip(), sys.stdin.readlines()))

height = len(mymap)
width = len(mymap[0])

totals = []


def get_at(mymap, posx, posy):
    line = mymap[posy]
    return line[posx % width]


pats = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
(patx, paty) = (3, 1)

for (patx, paty) in pats:
    total = 0
    (posx, posy) = (patx, paty)
    while posy < height:
        if get_at(mymap, posx, posy) == '#':
            total += 1
        posx += patx
        posy += paty

    totals.append(total)

product = 1

for total in totals:
    product *= total

print(totals)
print(product)
