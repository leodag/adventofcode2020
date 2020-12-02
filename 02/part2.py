import sys

lines = sys.stdin.readlines()

total = 0

def get_at(str, pos):
    try:
        return str[pos]
    except:
        return None

for line in lines:
    [policy, password] = line.split(':', maxsplit=1)
    password = password.strip()
    [rng, letter] = policy.split(' ')
    [low, high] = rng.split('-')
    low = int(low)
    high = int(high)

    first = get_at(password, low - 1) == letter
    second = get_at(password, high - 1) == letter
    if (first or second) and not (first and second):
        total += 1

print(total)
