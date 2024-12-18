from copy import copy
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

def run_program(opcodes, regs):
    running = True
    inc_ptr = True
    inst_ptr = 0
    output = []
    while(running):

        if not inst_ptr + 1 < len(opcodes):
            break

        combos = {0:0, 1:1, 2:2, 3:3, 4:regs['A'], 5:regs['B'], 6:regs['C']}
        op = int(opcodes[inst_ptr])

        ope = int(opcodes[inst_ptr+1])
        combo_ope = combos[ope]
        literal_ope = ope

        if op == 0:
            regs['A'] = int(float(regs['A']) / float((2**combo_ope)))
        elif op == 1:
            regs['B'] = regs['B'] ^ literal_ope
        elif op == 2:
            regs['B'] = combo_ope % 8
        elif op == 3:
            if regs['A'] != 0:
                inst_ptr = literal_ope
                inc_ptr = False
        elif op == 4:
            regs['B'] = regs['C'] ^ regs['B']
        elif op == 5:
            output.append(combo_ope % 8)
            # yield combo_ope % 8
        elif op == 6:
            regs['B'] = int(float(regs['A']) / float((2**combo_ope)))
        elif op == 7:
            regs['C'] = int(float(regs['A']) / float((2**combo_ope)))

        if inc_ptr:
            inst_ptr += 2
        else:
            inc_ptr = True

    return output

# Had to take some inspiration from github....
def solve(regs, prog):
    if not prog:
        yield regs['A']
    else:
        old = regs['A']
        for i in range(8):
            regs['A'] = (old << 3) | i
            print(regs)
            print(prog)
            out = run_program(prog, copy(regs))
            if out and out[0] == prog[-1]:
                yield from solve(copy(regs), prog[:-1])


regs = {'A':0, 'B':0, 'C':0}
solutions = list(solve(regs, [int(i)for i in opcodes]))
print('Part 2:', min(solutions))
print(iter)

f.close()
