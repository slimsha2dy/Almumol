import sys
from heapq import heappop
from heapq import heappush

for _ in range(int(input())):
    n, d, c = map(int, sys.stdin.readline().split())
    c -= 1
    adj = [[] for _ in range(n)]

    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        a -= 1
        b -= 1
        adj[b].append((s, a))

    heap = []
    visited = [False] * n
    dist = [sys.maxsize] * n
    dist[c] = 0
    count = 1
    answer = 0

    for next_d, next in adj[c]:
        dist[next] = next_d
        heappush(heap, (next_d, next))

    while heap:
        cur_d, cur = heappop(heap)

        if visited[cur]:
            continue

        visited[cur] = True
        count += 1
        answer = max(answer, cur_d)

        for next_d, next in adj[cur]:
            if dist[next] > cur_d + next_d:
                dist[next] = cur_d + next_d
                heappush(heap, (dist[next], next))

    print(count, answer)

