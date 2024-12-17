s = input()

stack = [0]
count = 0
prev = False

for c in s:
    if c == '(':
        stack.append(stack[-1] + 1)
        prev = True
    else:
        stack.pop()
        count += (stack[-1] if prev else 1)
        prev = False

print(count)
