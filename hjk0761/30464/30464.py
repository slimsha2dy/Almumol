import sys

n = int(input())
a = list(map(int, sys.stdin.readline().strip().split()))
dp = [-1 for _ in range(n)]

dp[0] = 0

for i in range(n-1):
    if dp[i] != -1:
        if i+a[i] < n:
            dp[i+a[i]] = dp[i] + 1

for i in range(n-2, -1, -1):
    if dp[i] != -1:
        if i-a[i] >= 0:
            dp[i-a[i]] = max(dp[i-a[i]], dp[i] + 1)

for i in range(n-1):
    if dp[i] != -1:
        if i+a[i] < n:
            dp[i+a[i]] = max(dp[i+a[i]], dp[i] + 1)

print(dp[n-1])
