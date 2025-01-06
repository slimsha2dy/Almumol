import sys

n, m = map(int, input().split())

field = list(map(int, sys.stdin.readline().strip().split()))
dp = [0 for _ in range(n+1)]

for i in range(m):
    a, b, k = map(int, sys.stdin.readline().strip().split())
    dp[a-1] += k
    dp[b] -= k

for i in range(1, n):
    dp[i] += dp[i-1]

for i in range(n):
    field[i] = field[i] + dp[i]

print(*field)
