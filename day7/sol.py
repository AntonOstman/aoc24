import itertools
f = open("input")

lines = f.read().split("\n")[0:-1]

total = 0

def create_all_operations(num):

    operations = list(itertools.product(*[['*','+'] for _ in range(num)]))
    return operations

for line in lines:
    ans, nums = line.split(': ')
    nums = nums.split(" ")
    already_added = False

    possible_positions = len(nums) - 1
    operations = create_all_operations(possible_positions)
    res = 0
    for ops in operations:
        val = int(nums[0])
        start_idx = 0
        for i in range(len(ops)):
            op = ops[i]
            a = int(nums[i + 1])

            if op == '*':
                if val == 0:
                    val = a
                else:
                    val *= a

            if op == '+':
                val += a

        if val == int(ans) and not already_added:
            already_added = True
            total += val


print(total)

f.close()
