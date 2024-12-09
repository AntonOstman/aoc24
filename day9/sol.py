f = open("input")

lines = f.read().split("\n")[0:-1]

disk = []
id = 0

for i, num in enumerate(lines[0]):
    if i % 2 == 0:
        disk.append([id] * int(num))
        id += 1
    if i % 2 == 1:
        disk.append(['.']*int(num))

for br, block_r in enumerate(disk[::-1]):
    if br % 2 == 1:
        continue
    for i, num_r in enumerate(block_r):
        if block_r[len(block_r) - i - 1] == '.':
            continue
        for bl, block_l in enumerate(disk):
            if bl % 2 == 0:
                continue
            if bl >= len(disk) - br:
                continue
            for j, num_l in enumerate(block_l):

                if num_l != '.':
                    continue
                if block_r[len(block_r) - i - 1] == '.':
                    continue
                if block_l[j] != '.':
                    continue

                tmp = block_l[j]
                block_l[j] = block_r[len(block_r) - i - 1]
                block_r[len(block_r) - i - 1] = tmp

disk_nums = [y for x in disk for y in x]

total = 0

for i, id in enumerate(disk_nums):
    if id != '.':
        total += i * int(id)

print(total)


f.close()
