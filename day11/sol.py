f = open("input")

lines = f.read().split("\n")[0:-1]

def blink(numbers):
    new_numbers = []
    for number in numbers:
        if number == '0':
            new_numbers.append('1')
        elif len(number) % 2 == 0:
            new_numbers.append(str(int(number[:len(number) // 2])))
            new_numbers.append(str(int(number[len(number) // 2:])))
        elif len(number) % 2 == 1:
            new_numbers.append(str(int(number) * 2024))
    return new_numbers

for line in lines:
    numbers = line.split(" ")
    nums = blink(numbers)
    for i in range(24):
        nums = blink(nums)

    print(len(nums))


f.close()
