from collections import deque, defaultdict
f = open("input.txt")

lines = f.read().strip().split("\n")
secrets = []
for line in lines:
    secrets.append(int(line))

def mix(num, secret):
    return num ^ secret

def prune(num):
    return num % 16777216

sequences = {}
prev_num = {}
nums = defaultdict(int)
used_seqs = defaultdict(set)

for j in range(2000):

        for i in range(len(secrets)):
            secret = secrets[i]
            # Could use bit shifts instead for speed... but meh
            # Step 1
            secret = prune(mix(secret * 64, secret))
            # Step 2
            secret = prune(mix(secret // 32, secret))
            # Step 3
            secret = prune(mix(secret*2048, secret))
            secrets[i] = secret

            last_num = secrets[i]%10
            if i not in sequences:
                sequences[i] = (last_num,)
                prev_num[i] = last_num
            elif len(sequences[i]) < 4:
                sequences[i] = sequences[i] + (last_num - prev_num[i],) 
                prev_num[i] = last_num
            else:
                sequences[i] =  sequences[i][1:4] + (last_num - prev_num[i],)
                if sequences[i] not in used_seqs[i]:
                    used_seqs[i].add(sequences[i])
                    nums[sequences[i]] += last_num
                prev_num[i] = last_num


print('part 1', sum(secrets))
print('part 2', max(nums.values()))

f.close()
