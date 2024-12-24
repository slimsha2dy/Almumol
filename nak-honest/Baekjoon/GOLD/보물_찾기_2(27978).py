import sys
from heapq import heappop
from heapq import heappush

H, W = map(int, input().split())
maps = [list(str(sys.stdin.readline().rstrip('\n'))) for _ in range(H)]

answer = sys.maxsize
start = (0, 0)
step = [(0, 1), (1, 1), (-1, 1), (0, -1), (1, 0), (1, -1), (-1, 0), (-1, -1)]

for i in range(H):
    for j in range(W):
        if maps[i][j] == 'K':
            start = (i, j)
            maps[i][j] = '.'


heap = []
visited = [[False] * W for _ in range(H)]
heap.append((0, start))
visited[start[0]][start[1]] = True

while heap:
    d, node = heappop(heap)
    i, j = node
    if maps[i][j] == '*':
        answer = min(answer, d)

    for diff_i, diff_j in step:
        next_i = diff_i + i
        next_j = diff_j + j

        if 0 <= next_i < H and 0 <= next_j < W and not visited[next_i][next_j] and maps[next_i][next_j] != '#':
            next_d = d
            if diff_j != 1:
                next_d += 1
            heappush(heap, (next_d, (next_i, next_j)))
            visited[next_i][next_j] = True

if answer == sys.maxsize:
    answer = -1

print(answer)
