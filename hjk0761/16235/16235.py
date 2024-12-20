import sys
from collections import deque

n, m, k = map(int, input().split())
a = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    a[i] = list(map(int, sys.stdin.readline().strip().split()))

ground = [[deque() for _ in range(n)] for _ in range(n)]
fertilizer = [[5 for _ in range(n)] for _ in range(n)]

for i in range(m):
    x, y, z = map(int, sys.stdin.readline().strip().split())
    ground[x-1][y-1].append(z)

dy = [1, 1, 1, 0, -1, -1, -1, 0]
dx = [1, 0, -1, -1, -1, 0, 1, 1]

def first():
    for i in range(n):
        for j in range(n):
            #spring
            live, dead = deque(), 0
            while ground[i][j]:
                tree = ground[i][j].popleft()
                if fertilizer[i][j] >= tree:
                    fertilizer[i][j] -= tree
                    live.append(tree+1)
                else:
                    dead += tree//2
            #summer
            fertilizer[i][j] += dead
            ground[i][j] = live

def second():
    for i in range(n):
        for j in range(n):
            #fall
            for tree in ground[i][j]:
                if tree % 5 == 0:
                    for k in range(8):
                        di, dj = i + dy[k], j + dx[k]
                        if di < 0 or dj < 0 or di >= n or dj >= n:
                            continue
                        ground[di][dj].appendleft(1)
            #winter
            fertilizer[i][j] += a[i][j]

for _ in range(k):
    first()
    second()

count = 0
for i in range(n):
    for j in range(n):
        count += len(ground[i][j])

print(count)
