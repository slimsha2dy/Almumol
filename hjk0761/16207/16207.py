import sys

n = int(input())

rods = list(map(int, sys.stdin.readline().strip().split()))

rods.sort(reverse=True)

made = set()
result = 0

for i in range(n-3):
    if i in made:
        continue
    a, b = rods[i], rods[i+1]
    if a - b > 1:
        continue
    long_side = a if a == b else b
    for j in range(i+2, n-1):
        if j in made:
            continue
        c, d = rods[j], rods[j+1]
        if c - d > 1:
            continue
        small_side = c if c == d else d
        result += long_side * small_side
        made.update([i, i+1, j, j+1])
        break

print(result)
