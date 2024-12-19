import sys
PRIME = 1_000_000_007

N = int(input())
scovil = sorted(list(map(int, sys.stdin.readline().split())))
diffs = [scovil[i+1] - scovil[i] for i in range(len(scovil) - 1)]

cur = sum(diffs)
d = [cur]

l = 0
r = N - 2

while l + 1 < r:
    cur -= diffs[l] + diffs[r]
    d.append((d[-1] + cur) % PRIME)
    l += 1
    r -= 1

if len(diffs) % 2 == 0:
    d = d + list(reversed(d))
else:
    d = d + list(reversed(d[:len(d)-1]))

answer = 0

for i in range(len(d)):
    answer += d[i] * pow(2, i, PRIME)
    answer %= PRIME

print(answer)
'''
scovil = 1 4 5 5 6 10
diffs = 3 1 0 1 4 4

다음과 같이 대칭 형태임

13 * 1
19 * 2
20 * 4
20 * 8
19 * 16
13 * 32


3 1 0 1 4 = 9
(4 1 1 5) * 2 = 11
(4 2 5) * 4 = 11
(5 6) * 8 = 11
(9) * 16 = 9
2 5 8

3 1 0 1 4
'''
