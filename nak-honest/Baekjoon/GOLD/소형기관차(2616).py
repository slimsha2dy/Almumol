import sys

N = int(input())
trains = list(map(int, sys.stdin.readline().split()))
max_t = int(input())

part_sum = [sum(trains[:max_t])]

for i in range(max_t, N):
    part_sum.append(part_sum[-1] + trains[i] - trains[i - max_t])

answer = 0
dp = [[0] * 3 for _ in range(N)]

dp[max_t-1][0] = part_sum[0]
for i in range(max_t, N):
    dp[i][0] = max(dp[i-1][0], part_sum[i-max_t+1])

# 밑에 2개는 묶을 수 있을 거 같은데 귀찮아서 안함
for i in range(max_t * 2 - 1, N):
    dp[i][1] = max(dp[i - 1][1], dp[i - max_t][0] + part_sum[i - max_t + 1])

for i in range(max_t * 3 - 1, N):
    dp[i][2] = max(dp[i - 1][2], dp[i - max_t][1] + part_sum[i - max_t + 1])
    answer = max(answer, dp[i][2])

print(answer)
'''
dp[i][c] = 0~i 까지의 객차들 중 c개의 기관차로 끌 수 있는 최대 인원 수


35 40 50 10 30 45 60 70 30 20 45 20


0   0   0
75  0   0
90  0   0
90  135 0
90  135

dp[i][c] = max(dp[i-1][c], dp[i-max_t][c-1] + part_sum[i-max_t+1])
'''
