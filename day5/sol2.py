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
for order in orders:
    numbers = order.split(',')
    fail = False
    preceding_numbers = []

    incorrect = False
    for number in numbers:
        if number not in rules:
            preceding_numbers.append(number)
            continue
        new_rules = rules[number]

        moved = len(preceding_numbers) 
        for preceding in preceding_numbers:
            if preceding in new_rules:
                fail = True
                incorrect = True
                while(fail):
                    if moved == len(preceding_numbers):
                        if preceding in preceding_numbers[0:]:
                            moved -= 1
                        else:
                            fail = False
                    else:
                        if preceding in preceding_numbers[0:moved]:
                            moved -= 1
                        else:
                            fail = False


        preceding_numbers.insert(moved, number)

    if incorrect:
        total += int(preceding_numbers[len(preceding_numbers) // 2])

print(total)
f.close()
