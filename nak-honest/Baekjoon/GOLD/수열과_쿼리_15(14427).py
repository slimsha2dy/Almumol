import sys
from heapq import heappop
from heapq import heappush
from heapq import heapify

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
M = int(input())

heap = []
for i in range(len(A)):
    heappush(heap, (A[i], i))

for _ in range(M):
    queries = list(map(int, sys.stdin.readline().split()))

    if queries[0] == 1:
        i, v = queries[1:]
        A[i-1] = v
        heappush(heap, (v, i-1))
    else:
        while A[heap[0][1]] != heap[0][0]:
            heappop(heap)
        print(heap[0][1] + 1)
