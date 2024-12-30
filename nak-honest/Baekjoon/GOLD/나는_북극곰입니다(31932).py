import sys
from collections import deque
from heapq import heappush
from heapq import heappop

N, M = map(int, input().split())

adj_list = [[] for _ in range(N)]
answer = 0
diff = 0

for _ in range(M):
    u, v, d, t = map(int, sys.stdin.readline().split())
    u -= 1
    v -= 1

    diff = max(diff, t)

    adj_list[u].append((d, v, t))
    adj_list[v].append((d, u, t))

for i in range(N):
    adj_list[i].sort()

def can_go(time):
    heap = []
    visited = [False] * N
    heap.append((0, 0, time))
    dist = [sys.maxsize] * N
    dist[0] = 0
    for node in adj_list[0]:
        if node[2] >= time + node[0]:
            if node[1] == N - 1:
                return True
            dist[node[1]] = node[0]
            heappush(heap, (node[0], node[1], time + node[0]))

    while heap:
        cur_dist, node, cur_time = heappop(heap)
        if node == N - 1:
            return True

        if visited[node]:
            continue
        visited[node] = True

        for _d, next_node, next_time in adj_list[node]:
            if cur_time + _d > next_time or visited[next_node]:
                continue
            if dist[next_node] > cur_dist + _d:
                dist[next_node] = cur_dist + _d
                heappush(heap, (cur_dist + _d, next_node, cur_time + _d))

    return False

diff //= 2

while diff > 1:
    if can_go(answer + diff):
        answer += diff

    diff //= 2

while can_go(answer + 1):
    answer += 1

if not can_go(0):
    answer = -1

print(answer)
