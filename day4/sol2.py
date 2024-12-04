f = open("input")

lines = f.read().strip().split()

total = 0

vis = list("."*140*140)
for i, line in enumerate(lines):

    for j, letter in enumerate(line):
        left = ""
        right = ""

        if (j + 2 < len(lines[i]) and i + 2 < len(lines)):
            right = lines[i][j] + lines[i+1][j+1] + lines[i+2][j+2]

        if (j + 2 < len(lines) and i + 2 < len(lines)):
            left = lines[i][j + 2] + lines[i+1][j+1] + lines[i+2][j]

        if ((left == "MAS" or left == "SAM") and (right == "MAS" or right == "SAM")):
            total += 1


print(total)
f.close()
