import sys

L, N, K = map(int, input().split())
charges = [0] + list(map(int, sys.stdin.readline().split()))
charges.append(L)

def can_go(bat):
    count = 0
    cur = 0
    for i in range(len(charges) - 1):
        if charges[i+1] - charges[i] > bat:
            return False
        if charges[i+1] - cur > bat:
            count += 1
            cur = charges[i]
            if count > K:
                return False

    return True


battery = L
diff = L // 2

while diff > 1:
    if can_go(battery - diff):
        battery -= diff

    diff //= 2

while can_go(battery - 1):
    battery -= 1

print(battery)
