import sys
from bisect import bisect_left

N = int(input())

lines = list(map(int, sys.stdin.readline().split()))

sorted_info = []
for line in lines[-1::-1]:
    line = -line
    i = bisect_left(sorted_info, line)
    if i == len(sorted_info):
        sorted_info.append(line)
    elif sorted_info[i] > line:
        sorted_info[i] = line

print(N - len(sorted_info))

'''
4 8 7 3 6 5 2 1 9
                1
              2             
            2
          2
        2
      3
    2
  2
3
[9, 8, 4]
'''
