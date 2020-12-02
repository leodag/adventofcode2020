import sys

numbers = list(map(lambda n: int(n), sys.stdin.readlines()))

amount = len(numbers)

partialsum = 0
target = 2020

for i in range(0, amount):
    if numbers[i] < target:
        for j in range(i + 1, amount):
            if numbers[i] + numbers[j] < target:
                for k in range(j + 1, amount):
                    if numbers[i] + numbers[j] + numbers[k] == target:
                        print(numbers[i] * numbers[j] * numbers[k])
                        break
