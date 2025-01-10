import sys

n = int(input())

cards = list(map(int, sys.stdin.readline().strip().split()))

cards.sort(reverse=True)

first = cards[0]
second = -1
count = 1

for i in range(1, n):
    if cards[i] != first:
        second = cards[i]
        break
    else:
        count += 1

if count % 2 == 1:
    print("koosaga")
elif second != -1:
    print("koosaga")
else:
    print("cubelover")
