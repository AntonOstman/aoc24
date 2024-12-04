def evaluate_line(nums):
    number_safe = 0
    ascending = False
    descending = False
    failed = False

    for i in range(len(nums)):
        if i == 0:
            continue
        prev = nums[i - 1]
        num = nums[i]

        if prev == num - 3 or prev == num - 2 or prev == num - 1:
            descending = True
        if prev == num + 3 or prev == num + 2 or prev == num + 1:
            ascending = True

        if prev > num + 3:
            failed = True
        elif prev < num - 3:
            failed = True
        if prev == num:
            failed = True
        if ascending and descending:
            failed = True

    if (not failed) and (descending ^ ascending):
        number_safe += 1

    return number_safe

f = open("input")

lines = f.read().split("\n")[0:-1]
safe = 0

for str_num in lines:
    nums = [int(i) for i in str_num.split(" ")]
    new_safe = 0
    print(nums)
    for i in range(len(nums)):
        nums.pop(i)
        print(nums)
        new_safe += evaluate_line(nums)
        nums = [int(i) for i in str_num.split(" ")]

    if new_safe > 0:
        safe += 1


print(safe)
