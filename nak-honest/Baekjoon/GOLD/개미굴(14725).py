import sys

N = int(input())

foods = sorted([sys.stdin.readline().split()[1:] for _ in range(N)])
max_len = len(max(foods, key=lambda x: len(x)))
visited = [set() for _ in range(max_len)]

def print_food(food, start):
    for i in range(start, len(food)):
        visited[i].add(food[i])
        print("--" * i + food[i])

prev_food = []
for food in foods:
    for i in range(len(food)):
        if i == len(prev_food):
            print_food(food, i)
            prev_food = food
            break
        elif prev_food[i] == food[i]:
            continue
        else:
            print_food(food, i)
            prev_food = food
            break
