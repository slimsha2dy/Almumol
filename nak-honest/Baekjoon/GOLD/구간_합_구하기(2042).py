import sys
from bisect import bisect_left

N, M, K = map(int, input().split())
nums = [int(sys.stdin.readline()) for _ in range(N)]
nu_sum = [nums[0]]
for i in range(1, N):
    nu_sum.append(nu_sum[-1] + nums[i])

diffs = []

for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        b -= 1
        diff = c - nums[b]

        i = bisect_left(diffs, [b, -sys.maxsize])
        if i == len(diffs) or diffs[i][0] != b:
            diffs.insert(i, [b, diff])
        else:
            diffs[i][1] = diff
    else:
        b -= 1
        c -= 1

        answer = nu_sum[c]
        if b > 0:
            answer -= nu_sum[b-1]

        l = bisect_left(diffs, [b, -sys.maxsize])
        r = bisect_left(diffs, [c, -sys.maxsize])

        if l == len(diffs) and r == len(diffs):
            print(answer)
        elif r == len(diffs):
            for i in range(l, len(diffs)):
                answer += diffs[i][1]
            print(answer)
        elif diffs[r][0] == c:
            for i in range(l, r+1):
                answer += diffs[i][1]
            print(answer)
        else:
            for i in range(l, r):
                answer += diffs[i][1]
            print(answer)


'''
1 2 3 4 5 6 7 8
1 2 5 4 1 6 10 8 = 36


8 1 4
1
2
3
4
5
6
7
8
1 3 5
1 5 1
1 7 6
1 7 10
2 6 8

(2, 3), (4, -4) (6, -1)

5~7 : 36


'''
