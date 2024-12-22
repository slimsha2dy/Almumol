PRIME = 10_007
fact = [1]
for i in range(1, 53):
    fact.append((fact[-1] * i))

def com(n, r):
    return (fact[n] % PRIME) * pow(fact[r] * fact[n-r], PRIME-2, PRIME) % PRIME

N = int(input())
k = N // 4

if N < 4:
    print(0)
else:
    answer = 13 * com(52-4, N-4)
    for i in range(1, k):
        answer += ((-1) ** i) * com(13, i+1) * com(52-4*(i+1), N - 4 * (i+1))
        answer %= PRIME

    print(answer % PRIME)

'''
1~3 : 0
4~7 : 1쌍 + N-4 조합
8~11 : 1쌍 + N-4 조합 - 2쌍 + N-8 조합
12~15 : 1쌍 + N-4 조합 - 2쌍 + N-8 조합 + (3쌍 + N - 12 조합)
16~19 : 1쌍 + N-4 조합 - 2쌍 + N-8 조합 + (3쌍 + N - 12 조합) - (4쌍 + N - 16 조합)

4 * k ~ 4 * k + 3 : (1쌍 + N-4 조합) - (2쌍 + N-8조합) + ... + (-1) ^ (k-1) * (k쌍 + N - 4*k 조합)
'''