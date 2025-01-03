import sys

N, M = map(int, input().split())
edges = []
length = []
fw = [[sys.maxsize] * N for _ in range(N)] # 플로이드 워셜

for _ in range(M):
    S, E, L = map(int, sys.stdin.readline().split())
    S -= 1
    E -= 1
    edges.append((S, E))
    length.append(L)
    fw[S][E] = min(fw[S][E], L)
    fw[E][S] = min(fw[E][S], L)

for i in range(N):
    fw[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if fw[i][k] != sys.maxsize and fw[k][j] != sys.maxsize:
                fw[i][j] = min(fw[i][j], fw[i][k] + fw[k][j])

answer = sys.maxsize

for i in range(N):
    time = 0
    for j in range(len(edges)):
        s, e = edges[j]
        max_t = max(fw[i][s], fw[i][e])
        min_t = min(fw[i][s], fw[i][e])

        if max_t - min_t >= length[j]:
            time = max(time, min_t + length[j])
        else:
            time = max(time, min_t + (max_t - min_t) + (length[j] - max_t + min_t) / 2)

        # 이거 없으면 python3에서 시간 초과 남
        if time >= answer:
            break

    answer = min(answer, time)

print(f"{answer:.1f}")

'''
1, 2, 4, 3
1, 5

S, E
-> S 도착 시간, E 도착 시간을 알면?
-> 길이가 L이라 하자. 그리고 min, max로 나누면
-> max - min >= L 인 경우에는 태우는데 L 초 걸림
-> max - min < L 인 경우에는 (max - min) + (L - (max - min)) / 2 초 걸림
'''


'''
직접 구한 방식.. 효율성에서 터짐

def bfs(start):
    cur_length = length[:]
    cur_adj_edges = deepcopy(adj_edges)
    time = 0
    one = set()
    half = set()

    for i in cur_adj_edges[start]:
        if edges[i][0] == edges[i][1]:
            half.add(i)
        else:
            one.add(i)
    cur_adj_edges[start].clear()

    while one or half:
        time += 1
        for i in half.copy():
            cur_length[i] -= 1
            if cur_length[i] == 0:
                half.remove(i)

        if time % 2 == 0:
            for i in one.copy():
                cur_length[i] -= 1
                if cur_length[i] == 0:
                    one.discard(i)
                    cur_adj_edges[edges[i][0]].discard(i)
                    cur_adj_edges[edges[i][1]].discard(i)

                    for j in cur_adj_edges[edges[i][0]].copy():
                        if j in one:
                            one.remove(j)
                            half.add(j)
                        else:
                            if edges[j][0] == edges[j][1]:
                                half.add(j)
                            else:
                                one.add(j)
                        cur_adj_edges[edges[i][0]].remove(j)

                    for j in cur_adj_edges[edges[i][1]].copy():
                        if j in one:
                            one.remove(j)
                            half.add(j)
                        else:
                            if edges[j][0] == edges[j][1]:
                                half.add(j)
                            else:
                                one.add(j)
                        cur_adj_edges[edges[i][1]].remove(j)

        for i in half.copy():
            if cur_length[i] == 0:
                half.remove(i)

    return time / 2
'''
