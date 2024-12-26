import sys

t = int(input())
result = []

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    graph = list(map(int, sys.stdin.readline().strip().split()))
    graph = list(map(lambda x:x-1, graph))
    visited = set()
    count = 0
    for i in range(n):
        node = graph[i]
        if node in visited:
            continue
        visited.add(node)
        count += 1
        next = node
        while graph[next] not in visited:
            next = graph[next]
            visited.add(next)
    result.append(count)

for re in result:
    print(re)
