import sys
from heapq import heappop
from heapq import heappush

# 다 최대로 몰아넣고, 공격과 방어의 차이가 작은 애들을 넘긴다.
for _ in range(int(input())):
    n, k = map(int, input().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))

    total = 0
    team_a = []
    team_b = []

    for i in range(n):
        if A[i] >= B[i]:
            heappush(team_a, (A[i] - B[i], i))
            total += A[i]
        else:
            heappush(team_b, (B[i] - A[i], i))
            total += B[i]

    while len(team_a) - len(team_b) > k:
        diff, i = heappop(team_a)
        heappush(team_b, (diff, i))
        total -= diff

    while len(team_b) - len(team_a) > k:
        diff, i = heappop(team_b)
        heappush(team_a, (diff, i))
        total -= diff

    print(total)
