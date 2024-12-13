import numpy as np
import re

f = open('input')

lines = f.read().splitlines()

ans = 0

for i in range(0, len(lines), 4):

    # Parse inputs
    equation = lines[i].split(": ")[1]
    nums = re.search('\+(\d*).*\+(\d*)', lines[i])
    equation = lines[i+1].split(": ")[1]
    c,e = nums.groups()
    nums = re.search('\+(\d\d).*\+(\d\d)', lines[i+1])
    d,f = nums.groups()
    nums = re.search('\=(\d*).*\=(\d*)', lines[i+2])
    b1, b2 = nums.groups()

    c = int(c)
    e = int(e)
    d = int(d)
    f = int(f)
    b1 = int(b1) + 10000000000000
    b2 = int(b2) + 10000000000000

    A = np.array([[c,d],
                  [e,f]])
    b = np.array([[b1],[b2]])
    # sol = np.linalg.solve(A,b)
    sol = np.linalg.inv(A) @ b

    a,b = round(sol[0,0]), round(sol[1,0])

    # Trick is to check if computing the price again with rounded values
    # gives the same prices back, as it should for a valid solution of only integers
    # I tried with np.isclose with a tolerance but that did not work either
    # I also checked if A was well continioed if that was an issue, but did not seem like it

    b1_round = a * c + b * d
    b2_round = a * e + b * f

    if b1 == b1_round and b2 == b2_round:
        ans += 3 * sol[0]
        ans += sol[1]
    

print(int(ans))
