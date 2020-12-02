import sys

lines = sys.stdin.readlines()

total = 0

for line in lines:
    [policy, password] = line.split(':', maxsplit=1)
    password = password.strip()
    [rng, letter] = policy.split(' ')
    [low, high] = rng.split('-')
    low = int(low)
    high = int(high)
    if password.count(letter) in range(low, high + 1):
        total += 1

print(total)
