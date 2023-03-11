import sys
N = int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline().strip()) for _ in range(N)]

max = arr[-1]
first = N-1
count = 1

for i in range(N):
    if arr[first-i] > max:
        max = arr[first-i]
        count += 1

print(count)