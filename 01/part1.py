import sys

numbers = list(map(lambda n: int(n), sys.stdin.readlines()))

amount = len(numbers)

for i in range(0, amount):
    for j in range(i + 1, amount):
        if numbers[i] + numbers[j] == 2020:
            print(numbers[i] * numbers[j])
            break;
