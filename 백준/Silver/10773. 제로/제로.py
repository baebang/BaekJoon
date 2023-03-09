import sys
num  = int(sys.stdin.readline())
arr = []
for i in range(num):
    a = int(sys.stdin.readline())
    if a > 0:
        arr.append(a)
    else:
        arr.pop()

print(sum(arr))