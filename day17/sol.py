import re
f = open("input")

lines = f.read()

registers, opcodes = lines.split("\n\n")
print(lines.split("\n\n"))

total = 0

regs = {}

for reg in registers.split("\n"):
    match = re.search("(.): (\d*)", reg)
    regs[match.groups()[0]] = int(match.groups()[1])
print(regs)


opcodes = opcodes.split(":")[1].strip()
opcodes = opcodes.split(",")



# def jnz(combo, reg)

inst_ptr = 0
running = True
inc_ptr = True
output = []
while(running):

    if inst_ptr >= len(opcodes):
        break

    combos = {0:0, 1:1, 2:2, 3:3, 4:regs['A'], 5:regs['B'], 6:regs['C']}
    op = int(opcodes[inst_ptr])

    # if inst_ptr == len(opcodes):
    if inst_ptr + 1 >= len(opcodes):
        assert False, 'kaos'
    ope = int(opcodes[inst_ptr+1])
    combo_ope = combos[ope]
    literal_ope = ope

    match(op):
        case 0:
            regs['A'] = int(float(regs['A']) / float((2**combo_ope)))
        case 1:
            regs['B'] = regs['B'] ^ literal_ope
        case 2:
            regs['B'] = combo_ope % 8
        case 3:
            if regs['A'] != 0:
                inst_ptr = literal_ope
                inc_ptr = False
            else:
                print('passing by')
                print(regs['A'])
        case 4:
            regs['B'] = regs['C'] ^ regs['B']
        case 5:
            output.append(combo_ope % 8)
        case 6:
            regs['B'] = int(float(regs['A']) / float((2**combo_ope)))
        case 7:
            regs['C'] = int(float(regs['A']) / float((2**combo_ope)))


    if inc_ptr:
        inst_ptr += 2
    else:
        inc_ptr = True

    
print(output)
print(",".join([str(i) for i in output]))
print("".join([str(i) for i in output]))


f.close()
