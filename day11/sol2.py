from collections import defaultdict 
f = open("input")

total = 0
lines = f.read().split("\n")[0:-1]

cache = defaultdict(int)

def blink(number, i, stop):
    i += 1
    if (number, i) in cache:
        return cache[(number, i)]
    if i == stop:
        return 1
    if number == '0':
        return blink('1', i, stop)
    elif len(number) % 2 == 0:
        ans = blink(str(int(number[:len(number) // 2])), i, stop) + blink(str(int(number[len(number) // 2:])), i, stop)
        cache[(number,i)] = ans
        return ans
    elif len(number) % 2 == 1:
        return blink(str(int(number) * 2024), i, stop)
    assert False, 'big err'

for line in lines:
    numbers = line.split(" ")
    for num in numbers:
        total += blink(num, -1, 75)

print(total)


f.close()
