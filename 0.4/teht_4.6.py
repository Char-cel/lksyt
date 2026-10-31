import random
i = 0
n = 0
N = 100000
x = random.uniform(-1, 1)
y = random.uniform(-1, 1)
while i < N:
    i += 1
    pi = 4 * n / N
    if x ** 2 + y ** 2 < 1:
        n +=  1
print(pi)