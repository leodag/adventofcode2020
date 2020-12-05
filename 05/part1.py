import sys

def parse_pass(bpass_str):
    row = bpass_str[:7].replace('F', '0').replace('B', '1')
    column = bpass_str[7:].replace('L', '0').replace('R', '1')
    return int(row, base=2), int(column, base=2)

def seat_id(bpass):
    (row, column) = bpass
    return row * 8 + column

lines = list(map(lambda s: s.strip(), sys.stdin.readlines()))

passes = list(map(lambda line: seat_id(parse_pass(line)), lines))

print(max(passes))
