import sys
import re

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


def validate_height(height):
    if height.endswith('cm'):
        val = int(height[:-2])
        return 150 <= val and val <= 193
    elif height.endswith('in'):
        val = int(height[:-2])
        return 59 <= val and val <= 76
    else:
        return False


valid_eyes = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

required = {
    'byr': lambda val: len(val) == 4 and 1920 <= int(val) and int(val) <= 2002,
    'iyr': lambda val: len(val) == 4 and 2010 <= int(val) and int(val) <= 2020,
    'eyr': lambda val: len(val) == 4 and 2020 <= int(val) and int(val) <= 2030,
    'hgt': validate_height,
    'hcl': lambda val: re.search("^#[0-9a-f]{6}$", val) is not None,
    'ecl': lambda val: val in valid_eyes,
    'pid': lambda val: re.search("^[0-9]{9}$", val) is not None
}

valid_count = 0

for passport in passports:
    valid = True
    for key, validator in required.items():
        value = passport.get(key)
        if value is None:
            valid = False
            break

        if not validator(value):
            valid = False
            break

    if valid:
        valid_count += 1

print(valid_count)
