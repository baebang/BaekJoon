import sys

N = int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline().strip()) for _ in range(N)]
max_val = arr[-1]
last_idx = N - 1
count = 1

for i in range(N):
    if arr[last_idx - i] > max_val:
        max_val = arr[last_idx - i]
        count += 1

print(count)
