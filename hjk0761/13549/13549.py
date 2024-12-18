import sys
from collections import deque

n, k = map(int, input().split())

time = [sys.maxsize for _ in range(100001)]

time[n] = 0

q = deque()
q.append(n)

while q:
    x = q.popleft()
    if x == k:
        break
    if x-1 >= 0:
        if time[x-1] > time[x] + 1:
            time[x-1] = time[x] + 1
            q.append(x-1)
    if x+1 <= 100000:
        if time[x+1] > time[x] + 1:
            time[x+1] = time[x] + 1
            q.append(x+1)
    if 2*x <= 100000:
        if time[2*x] > time[x]:
            time[2*x] = time[x]
            q.append(2*x)
print(time[k])
