import sys
from heapq import heappush
from heapq import heappop

n = int(input())
ho = [sorted(list(map(int, sys.stdin.readline().split()))) for _ in range(n)]

L_start = []
starts = set()

d = int(input())

for l, r in ho:
    if r - l > d:
        continue

    # L 의 시작점이 위치할 수 있는 범위를 각각 지정
    L_start.append((r-d, l))

    # L의 시작점 후보들(== 각 사람의 가장 왼쪽 위치)
    starts.add(l)

L_start.sort()
starts = sorted(starts)

answer = 0
heap = []
i = 0

# (몰랐는데 내가 푼 방식이 스위핑 방식이라고 한다.)
# 각 사람의 집과 사무실 위치에 대해 L의 시작점이 위치할 수 있는 범위를 (a, b) 라고 하자.
# 그러면 먼저 (a, b) 를 정렬하고, L의 시작점 후보인 start를 하나씩 가지고 와 비교한다.
# 먼저는 끝점인 b를 생각하지 않고, start가 a보다 크면 끝점인 b를 힙에 넣는다. -> (a, b)에 대해 정렬되어 있기 때문에 한번만 순차 탐색하면 됨!
# 다 넣은 후 힙에서 가장 작은 b가 start보다 작은지 계속 확인한다. start보다 끝점인 b가 작다는 것은 L의 범위를 벗어나는 것이기 때문에 힙에서 삭제한다.
# 그러면 start를 L의 시작점으로 했을 때 포함되는 사람들의 수는 힙의 크기가 된다.
for start in starts:
    while i < len(L_start) and L_start[i][0] <= start:
        heappush(heap, L_start[i][1])
        i += 1
    while heap and heap[0] < start:
        heappop(heap)

    answer = max(answer, len(heap))

print(answer)
