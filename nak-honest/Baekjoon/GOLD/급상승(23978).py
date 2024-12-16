import sys

def s(num):
    return (num * (num + 1)) // 2

N, K = map(int, input().split())
A = list(map(int, sys.stdin.readline().split()))

def can_sell(X):
    cur = X
    for i in range(len(A)-1):
        if A[i+1] - A[i] >= X:
            cur += s(X)
        else:
            cur += s(X) - s(X - A[i+1] + A[i])

    cur += s(X-1)
    return cur >= K

x = K // N + 1
diff = x // 2

while diff > 1:
    if can_sell(x - diff):
        x -= diff
    diff //= 2

while can_sell(x - 1):
    x -= 1

print(x)
