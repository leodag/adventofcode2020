import sys

lines = list(map(lambda s: s.strip(), sys.stdin.readlines()))

passports = []

passport = {}
for line in lines:
    if line == '':
        passports.append(passport)
        passport = {}
        continue

    fields = line.split(' ')
    for field in fields:
        [kind, value] = field.split(':', maxsplit=1)
        passport.update({kind: value})
passports.append(passport)

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid_count = 0

for passport in passports:
    valid = True
    for key in required:
        if passport.get(key) is None:
            valid = False
            break
    if valid:
        valid_count += 1

print(valid_count)
