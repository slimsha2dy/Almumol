import sys
import heapq

n, m = map(int, input().split())
gawang = [list(map(lambda x: x*-1, map(int, sys.stdin.readline().strip().split()))) for _ in range(n)]

for g in gawang:
    heapq.heapify(g)

def turn():
    second_winner = heapq.heappop(gawang[1])
    for i in range(1, n-1):
        winner = heapq.heappop(gawang[i+1])
        heapq.heappush(gawang[i], winner)
    first_loser = gawang[0].pop()
    heapq.heappush(gawang[-1], first_loser)
    heapq.heappush(gawang[0], second_winner)

for i in range(m if m <= n else n + (m % n)):
    turn()
for p1, p2 in gawang:
    print(p2*-1, p1*-1)
