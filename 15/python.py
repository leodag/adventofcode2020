def parse_file(name):
    line = open(name).read().splitlines()[0]
    return list(map(lambda s: int(s), line.split(",")))


def play(start, turns):
    turn = 1
    lastplayed = {}
    lastplay = 0

    for play in start:
        lastplayed[play] = (turn, 0)
        lastplay = play
        turn += 1

    while turn <= turns:
        prev, last = lastplayed.get(lastplay)
        if last != 0:
            play = prev - last
        else:
            play = 0

        prev2, last2 = lastplayed.get(play, (0, 0))
        lastplayed[play] = (turn, prev2)
        lastplay = play
        turn += 1

    return lastplay


def part1(filename="input"):
    return play(parse_file(filename), 2020)


def part2(filename="input"):
    return play(parse_file(filename), 30000000)
