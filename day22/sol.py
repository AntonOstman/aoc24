from collections import deque
f = open("input.txt")

lines = f.read().strip().split("\n")

secrets = []

for line in lines:
    secrets.append(int(line))


def mix(num, secret):
    return num ^ secret

def prune(num):
    return num % 16777216


for i in range(2000):
    print(secrets)
    for i in range(len(secrets)):
        secret = secrets[i]
        # Step 1
        secret = prune(mix(secret * 64, secret))
        #secret = prune(secret)
        # Step 2
        secret = prune(mix(secret // 32, secret))
        #secret = prune(secret)
        # Step 3
        secret = prune(mix(secret*2048, secret))
        # secret = prune(secret)
        secrets[i] = secret

print(sum(secrets))

f.close()
