import re
f = open("input")

lines = f.read().split("\n")[0:-1]

preceding_rules = {}

total = 0

num_rules = 0
rules = {}
orders = []

for line in lines:
    if line != '':
        num_rules += 1
        if line[0:2] not in rules:
            rules[line[0:2]] = [line[3:]]
        else:
            rules[line[0:2]] = rules[line[0:2]] + [line[3:]]
    else:
        break

orders = lines[num_rules + 1:]

preceding_numbers = []
for order in orders:
    numbers = order.split(',')
    fail = False
    preceding_numbers = []

    for number in numbers:
        if number not in rules:
            preceding_numbers.append(number)
            continue
        else:
            new_rules = rules[number]
            for preceding in preceding_numbers:
                if preceding in new_rules:
                    fail = True
        preceding_numbers.append(number)

    if not fail:
        total += int(numbers[len(numbers) // 2])


print(total)
f.close()
