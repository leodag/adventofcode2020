def parse_file(name):
    line = open(name).read().splitlines()[0]
    return list(map(lambda s: int(s), line.split(",")))


def play(start, turns):
    turn = 1
    lastplayed = {}

    for play in start:
        nextplay = lastplayed.get(play, 0)
        if nextplay != 0:
            nextplay = turn - nextplay

        lastplayed[play] = turn
        turn += 1

    while turn <= turns:
        play = nextplay
        nextplay = lastplayed.get(play, 0)
        if nextplay != 0:
            nextplay = turn - nextplay

        lastplayed[play] = turn
        turn += 1

    return play


def part1(filename="input"):
    return play(parse_file(filename), 2020)


def part2(filename="input"):
    return play(parse_file(filename), 30000000)
