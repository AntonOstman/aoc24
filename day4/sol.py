f = open("input")

lines = f.read().strip().split()

total = 0

vis = list("."*140*140)
for i, line in enumerate(lines):

    for j, letter in enumerate(line):

        if (i + 3 < len(lines)):
            word = lines[i][j] + lines[i+1][j] + lines[i+2][j] + lines[i+3][j] 
            if (word == "XMAS" or word[::-1] == "XMAS"):
                total += 1

        if (j + 3 < len(lines[i])):
            word = lines[i][j] + lines[i][j+1] + lines[i][j+2] + lines[i][j+3] 
            if (word == "XMAS" or word[::-1] == "XMAS"):
                total += 1

        if (j + 3 < len(lines[i]) and i + 3 < len(lines)):
            word = lines[i][j] + lines[i+1][j+1] + lines[i+2][j+2] + lines[i+3][j+3] 
            if (word == "XMAS" or word[::-1] == "XMAS"):
                total += 1

        if (j - 3 >= 0 and i + 3 < len(lines)):
            word = lines[i][j] + lines[i+1][j-1] + lines[i+2][j-2] + lines[i+3][j-3] 
            if (word == "XMAS" or word[::-1] == "XMAS"):
                total += 1


print(total)
f.close()
