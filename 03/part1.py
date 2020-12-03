import sys

mymap = list(map(lambda s: s.strip(), sys.stdin.readlines()))

height = len(mymap)
width = len(mymap[0])

total = 0


def get_at(mymap, posx, posy):
    line = mymap[posy]
    print(posx % width)
    return line[posx % width]


(patx, paty) = (3, 1)
(posx, posy) = (patx, paty)

while posy < height:
    if get_at(mymap, posx, posy) == '#':
        total += 1
    posx += patx
    posy += paty

print(total)
