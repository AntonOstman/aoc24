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

for br in range(len(disk)):
    if br % 2 == 1:
        continue
    block_handeled = False

    r_idx = len(disk) - br - 1
    for bl in range(len(disk)):
        if bl % 2 == 0:
            continue
        if bl >= r_idx:
            continue
        if block_handeled:
            break
        if disk[r_idx].count('.') > 0:
            continue

        if disk[bl].count('.') >= len(disk[r_idx]):
            block_handeled = True
            start = disk[bl].index('.')
            disk[bl][start:start + len(disk[r_idx])] = disk[r_idx]
            disk[r_idx] = ['.'] * len(disk[r_idx])

disk_nums = [y for x in disk for y in x]

total = 0

for i, id in enumerate(disk_nums):
    if id != '.':
        total += i * int(id)

print(total)


f.close()
