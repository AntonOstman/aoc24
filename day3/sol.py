import os
import subprocess
import re

# grep 'mul([0-9]*,[0-9]*)' input -o | grep '[0-9]*,[0-9]*' -o > clean-input
# part2 cat input2 | perl -pe "s/don\'t\(\).*?do\(\)//g" | grep 'mul([0-9]*,[0-9]*)' -o | grep '[0-9]*,[0-9]*' -o > clean-input22 && python3 sol.py
f = open("clean-input22")

lines = f.read().split("\n")[0:-1]


total = 0
for line in lines:
    numbers = line.split(",")
    if len(numbers) < 2 or line == ',':
        continue
    total += int(numbers[0]) * int(numbers[1])

print(total)

